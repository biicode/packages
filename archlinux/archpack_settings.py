#
# Biicode Arch Linux package settings.
# 
# Check PKGBUILD_template docs for those settings and 
# what they mean.
#

def settings():
	return { "version": "2.7",
			 "release_number": "1",
			 "arch_deps": ["cmake>=3.0.2", 
			                "zlib", 
			                "glibc", 
			                "sqlite", 
			                "wget",
                                        "python2-pmw"
			              ],
			 "debian_deps": ["zlib1g",
			                 "libc-bin",
			                 "libsqlite3-0",
			                 "wget",
			                 "lib32z1",
                                         "python-tk"
			                ]
			}

if __name__ == '__main__': 
    print(settings())
