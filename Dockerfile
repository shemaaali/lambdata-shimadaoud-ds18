FROM ubuntu
# So logging/io works reliably w/Docker
ENV PYTHONUNBUFFER=1
# Install/setup Python dependencies and lambdata
RUN apt update && \
  apt upgrade -y && \
  apt install python3 python3-pip curl -y && \
  pip3 install pandas && \              
  pip3 install -i https://test.pypi.org/simple/ lambdata-shimadaoud-ds18