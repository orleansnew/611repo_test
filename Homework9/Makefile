SUBDIRS = output py36

.PHONY: subdirs $(SUBDIRS)

subdirs: $(SUBDIRS)

$(SUBDIRS):
	mkdir -p $@


py36/Dockerfile: subdirs
	cp Dockerfile ./py36/
	docker build -t py36 ./py36

output/hw9_2.txt: hw9_1.py hw9_2.py hw9_3.py py36/Dockerfile 
	docker run -d --rm -v $(shell pwd):$(shell pwd) -w $(shell pwd) py36 `/bin/bash -c "python ./hw9_1.py 2 3 7 4 6 > output/hw9_1.txt"`
	docker run -d --rm -v $(shell pwd):$(shell pwd) -w $(shell pwd) py36 `/bin/bash -c "python ./hw9_2.py 5 2 17 > output/hw9_2.txt"`
	docker run -d --rm -v $(shell pwd):$(shell pwd) -w $(shell pwd) py36 `/bin/bash -c "python ./hw9_3.py  > output/hw9_3.txt"`


output/hw9_4.txt: hw9_4.py hw9_5.py subdirs
	docker pull frolvlad/alpine-python-machinelearning
	docker run -d frolvlad/alpine-python-machinelearning `/bin/bash -c "python hw9_4.py 0 1 2 > ./output/hw9_4.txt"`
	docker run -d frolvlad/alpine-python-machinelearning `/bin/bash -c "python hw9_5.py 3 5 > ./output/hw9_5.txt"`

.PHONY:makeall

makeall: output/hw9_4.txt output/hw9_2.txt 
	ls output/
