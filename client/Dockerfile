FROM ubuntu:18.04

# Install packages
RUN apt-get update && \
 apt install -qy \
  autoconf \
  automake \
  libtool \
  python3 \
  apt-utils \
  gcc \
  make \
  libssl-dev \
  unzip \
  git \
  wget \
  xsltproc \
  tcpdump \
  #vim \
  python3-pip

# Setup directories
RUN mkdir -p /client/
RUN mkdir -p /client/scripts
#RUN mkdir -p /client/results
# Copy liboqs and openssl to container

WORKDIR /client/
RUN git clone https://github.com/lrubens/openssl.git
VOLUME ["/client/openssl/results"]

WORKDIR /client/
RUN git clone https://github.com/lrubens/liboqs.git
VOLUME ["/client/scripts"]
#ADD client.py /client/scripts

# Install liboqs
WORKDIR /client/liboqs
RUN autoreconf -i
RUN ./configure --prefix=/client/openssl/oqs --with-openssl=/usr/lib/ssl --enable-shared=no
RUN make -j
RUN make install

# Install openssl
WORKDIR /client/openssl
RUN ./Configure no-shared linux-x86_64 -lm
RUN make -j

# Set working dir to root directory
WORKDIR /client/scripts/

