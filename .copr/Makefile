
srpm:
	git clone https://github.com/skilion/onedrive.git
	cp onedrive.spec onedrive
	( cd onedrive ; make version; rpkg make-source )
	cp onedrive-copr.patch onedrive
	( cd onedrive ; rpkg srpm )


clean: 
	rm -rf onedrive
