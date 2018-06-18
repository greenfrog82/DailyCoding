FROM centos:7

# update centos
RUN yum -y update
RUN yum -y upgrade

# [Begin] https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-centos-7
RUN yum -y install yum-utils
RUN yum -y groupinstall development

RUN yum -y install https://centos7.iuscommunity.org/ius-release.rpm
RUN yum -y install \
	python36u \
	python36u-pip \
	python36u-devel

# [End]

RUN ln -s /usr/bin/python3.6 /usr/bin/python3

RUN curl -sL https://rpm.nodesource.com/setup_8.x | bash -
RUN yum -y install nodejs

WORKDIR /develop