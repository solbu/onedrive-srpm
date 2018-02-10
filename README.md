# onedrive-srpm
The purpose of this repository is to provide a specif build environment to https://github.com/skilion/onedrive in Copr/build.

.copr/Makefile
  This is a core of the work. More information can be found at https://docs.pagure.org/copr.copr/user_documentation.html#make-srpm
  (1) install rpkg and git in order to have a working environment to produce the srpm package
  (2) retreive onedrive sources from https://github.com/skilion/onedrive.git
  (3) generate the version file from the git hierarchie
  (4) produce a rpkg Source 
  (5) patch the Makefile in order to remove .git related work ( version )
  (6) produce the rpkg srpm file and plate it on $(outdir) directory

