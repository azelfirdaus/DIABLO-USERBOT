# Using Python Slim-Buster
FROM xluxz/geezproject:buster
# RAM-UBOT
# Geez-UserBot
#yaudah iya

RUN git clone -b RAM-UBOT https://github.com/azelfirdaus/DIABLO-USERBOT /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/azelfirdaus/DIABLO-USERBOT/DIABLO-USERBOT/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3","-m","userbot"]
