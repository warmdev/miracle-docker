FROM centos:7

# Install dependencies
RUN yum -y update; yum clean all; yum -y install epel-release
RUN yum clean expire-cache; yum -y install selinux-policy; yum update selinux-policy\*
RUN yum -y install git python-pip python-devel postgresql-devel gcc pcre pcre-devel gdal python-pip libffi-devel openssl-devel
RUN pip install virtualenv virtualenvwrapper requests[security]; pip install http://projects.unbit.it/downloads/uwsgi-lts.tar.gz
# Setup users
RUN groupadd comses; useradd -r -G comses -u 1001 nginx
# Download miracle code
WORKDIR /opt
RUN mkdir virtualenvs; chown -R nginx:comses virtualenvs
ENV WORKON_HOME=/opt/virtualenvs
RUN git clone --depth 1 https://github.com/comses/miracle.git; \
	chown -R nginx:comses miracle
# Setup miracle app
USER nginx
RUN	cd miracle; source /usr/bin/virtualenvwrapper.sh; \
	mkvirtualenv miracle; workon miracle; pip install -Ur requirements.txt; deactivate
ADD local.py miracle/miracle/settings/local.py
ADD miracle.sh /opt/miracle/miracle.sh
ADD miracle.ini /opt/miracle/deploy/uwsgi/miracle.ini
USER root
RUN chmod +x /opt/miracle/miracle.sh; chown nginx:comses /opt/miracle/miracle.sh
RUN chown nginx:comses /opt/miracle/deploy/uwsgi/miracle.ini
USER nginx

#EXPOSE 8888

CMD /opt/miracle/miracle.sh