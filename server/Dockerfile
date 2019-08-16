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
  tcpdump

# Setup directories
RUN mkdir -p /server/

# Copy liboqs and openssl to container
WORKDIR /server/
RUN git clone https://github.com/lrubens/openssl.git

WORKDIR /server/
RUN git clone https://github.com/lrubens/liboqs.git
ADD server.py /server/openssl
# Install liboqs
WORKDIR /server/liboqs
RUN autoreconf -i
RUN ./configure --prefix=/server/openssl/oqs --with-openssl=/usr/lib/ssl --enable-shared=no
RUN make -j
RUN make install

# Install openssl
WORKDIR /server/openssl
RUN ./Configure no-shared linux-x86_64 -lm
RUN make -j

# Set working dir to root directory
WORKDIR /server/openssl

