#!/usr/bin/bash
chmod +x *.py
fpm \
	-s dir -t deb \
	-p nicedice.deb \
	--name nicedice \
	--license MIT \
	--version 0.1.0 \
	--architecture amd64 \
	--description "Software-defined dice simulation with the ability to create and share custom RNGs." \
	--url "https://github.com/PPPDUD/nicedice" \
	--maintainer "PPPDUD <mojavesoft@gmail.com>" \
	--depends python3 \
	--deb-recommends python3-questionary \
	nicedice.py=/usr/bin/nicedice \
	nicedice-create.py=/usr/bin/nicedice-create \
	dice/=/usr/share/nicedice/