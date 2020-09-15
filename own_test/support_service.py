import pytest
import operator


class  NoAgentFoundExcept(Exception):
    pass


class Ticket:
    def __init__(self, id, restrictions):
        self.id = id
        self.restrictions = restrictions


class Agent:
    def __init__(self, name, skills, load):
        self.name = name
        self.skills = skills
        self.load = load

    def __repr__(self):
        return f'{self.name} {self.skills} {self.load}'


class FinderPolicy(object):
    def _filter_loaded_agents(self, agents):
        agents = [agent for agent in agents if agent.load < 3]
        if not agents:
            raise NoAgentFoundExcept
        return agents

    def find(self, ticket, agents):
        pass


class LeastLoadedAgent(FinderPolicy):
    def find(self, ticket, agents):
        agents = self._filter_loaded_agents(agents)        
        return min(agents, key=lambda obj: obj.load)


class LeastFlexibleAgent(FinderPolicy):
    def find(self, ticket, agents):
        agents = self._filter_loaded_agents(agents)
        restrictions = set(ticket.restrictions)
        agents = [agent for agent in agents if set(agent.skills).issubset(restrictions)]
        if not agents:
            raise NoAgentFoundExcept
        return min(agents, key=lambda obj: obj.load)


@pytest.fixture
def ticket_and_agents():
    return (Ticket(id="1", restrictions=["English"]), 
            [Agent(name="A", skills=["English"], load=2), 
            Agent(name="B", skills=["English", "Japanese"], load=0)])


@pytest.fixture
def ticket_and_agents_all_agents_are_full_loaded():
    return (Ticket(id="1", restrictions=["English"]), 
            [Agent(name="A", skills=["English"], load=3), 
            Agent(name="B", skills=["English", "Japanese"], load=3)])


@pytest.fixture
def complex_ticket_and_agents():
    return (Ticket(id="1", restrictions=["English"]), 
            [Agent(name="A", skills=["English", "Japanese"], load=2), 
            Agent(name="B", skills=["English", "Japanese"], load=1),
            Agent(name="C", skills=["English", "Japanese", "Franch"], load=0),
            Agent(name="D", skills=["English", "Japanese"], load=0),
            Agent(name="E", skills=["English"], load=1),
            Agent(name="F", skills=["English"], load=2)])


def test_least_loaded_policy(ticket_and_agents):
    ticket, agents = ticket_and_agents
    least_loaded_policy = LeastLoadedAgent()
    # returns the Agent with name "B" because of their currently lower load.
    assert least_loaded_policy.find(ticket, agents) == agents[1]


def test_least_loaded_policy_there_are_no_agents(ticket_and_agents):
    ticket, _ = ticket_and_agents
    least_loaded_policy = LeastLoadedAgent()
    with pytest.raises(NoAgentFoundExcept):
        least_loaded_policy.find(ticket, [])


def test_least_loaded_policy_when_all_agents_are_full_loaded(ticket_and_agents_all_agents_are_full_loaded):
    ticket, agents = ticket_and_agents_all_agents_are_full_loaded
    least_loaded_policy = LeastLoadedAgent()
    with pytest.raises(NoAgentFoundExcept):
        least_loaded_policy.find(ticket, agents)


def test_flexible_policy(ticket_and_agents):
    ticket, agents = ticket_and_agents
    least_flexible_policy = LeastFlexibleAgent()
    # returns the Agent with name "A" because of their lower flexibility.
    least_flexible_policy.find(ticket, agents)


def test_complex_flexible_policy(complex_ticket_and_agents):
    ticket, agents = complex_ticket_and_agents
    least_flexible_policy = LeastFlexibleAgent()
    # returns the Agent with name "D" because of their lower flexibility.
    assert least_flexible_policy.find(ticket, agents) == agents[-2]

    
def test_flexible_policy_there_are_no_agents(ticket_and_agents):
    ticket, _ = ticket_and_agents
    least_flexible_policy = LeastFlexibleAgent()
    with pytest.raises(NoAgentFoundExcept):
        least_flexible_policy.find(ticket, [])


def test_flexible_policy_when_all_agents_are_full_loaded(ticket_and_agents_all_agents_are_full_loaded):
    ticket, agents = ticket_and_agents_all_agents_are_full_loaded
    least_flexible_policy = LeastFlexibleAgent()
    with pytest.raises(NoAgentFoundExcept):
        least_flexible_policy.find(ticket, agents)