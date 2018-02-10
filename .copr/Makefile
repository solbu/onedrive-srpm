
srpm:
	dnf install git make rpkg
	git clone https://github.com/skilion/onedrive.git
	( cd onedrive ; make version )
	cat onedrive.spec | sed -e "s/gitvers/$$(cat onedrive/version | sed s/v//)/" > onedrive/onedrive.spec
	rpkg --path onedrive make-source 
	cp onedrive-copr.patch onedrive
	rpkg srpm --spec onedrive/onedrive.spec --outdir $(outdir)


clean: 
	rm -rf onedrive
	rm -f onedrive.tar
	rm -f onedrive*.src.rpm	
