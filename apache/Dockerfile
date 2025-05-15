FROM httpd:2.4

RUN apt-get update && apt-get install -y \
    libapache2-mod-auth-ntlm \
    && a2enmod auth_ntlm \
    && rm -rf /var/lib/apt/lists/*

COPY ntlm.conf /usr/local/apache2/conf/extra/ntlm.conf
RUN echo "Include conf/extra/ntlm.conf" >> /usr/local/apache2/conf/httpd.conf
