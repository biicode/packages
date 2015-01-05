import archpack_settings
import hashlib , urllib.request
import sys

#
# Module for automatic generation of an AUR package for biicode
#
# To generate such package, a template PKGBUILD file (PKGBUILD_tenplate) is
# provided, with tags of the form <TAGS> specifying certain settings and
# metadata needed by the package script. See the docs inside PKGBUILD_template
# for the meaning of that tags.
# 
# An 'archpack_settings.py' module is provided with a dictionary contaning the
# settings of the package: Biicode version, dependencies, etc. 
# 
# A generator object takes that dictionary and uses it to apply the current
# settings to the PKGBUILD template, also generating and applying some extra
# metadata the PKGBUILD needs, such as the checksums of the packages (Note three
# platform are supported on Arch Linux, hence three source Debian packages).
#


class generator:
	"""Generates the PKGBUILD file and the AUR package
	   with the settings specified at archpack_settings.py"""

	settings = archpack_settings.settings()
	metadata = {}
						
						

	def __init__(self):
		self.process_settings()
		self.metadata = self.generate_metadata()

	def process_settings(self):
		"""Translates some settings from python syntax into the required PKGBUILD
		   syntax"""

		self.settings['arch_deps'] = '\'' + ('\' \''.join( self.settings['arch_deps'] )) + '\''
		self.settings['debian_deps'] = ','.join( self.settings['debian_deps'] )


	def generate_metadata(self):
		"""Generates the metadata required by the PKGBUILD script"""

		print('Generating metadata...')

		return { 'version_label': self.version_label(),
				 'sum_32': self.checksum('32'),
				 'sum_64': self.checksum('64'),
				 'sum_pi': self.checksum('pi'),
				 'pkg_prefix_32': self.package_prefix('32'),
				 'pkg_prefix_64': self.package_prefix('64'),
				 'pkg_prefix_pi': self.package_prefix('pi')
			   }


	def version_label(self):
		"""Returns the version of the package using underscores"""

		return self.settings['version'].replace('.','_')


	def package_prefix(self,platform):
		"""Returns the package name prefix given the platform"""

		return {'32': 'ubuntu-32',
				'64': 'ubuntu-64',
				'pi': 'debian-armv6'}[platform]

	def package_name(self,platform):
		"""Returns the name of the debian package, given the platform"""

		return 'bii-' + self.package_prefix(platform) + '_' + self.version_label() + '.deb'


	def package_url(self,platform):
		"""Retuns the URL of the hosted debian package, given the platform"""

		return 'https://s3.amazonaws.com/biibinaries/release/' + \
			   self.settings['version'] + '/' + self.package_name(platform)

		
	def checksum(self,platform):
		"""Returns the ckecksum of the debian package of the specified platform"""

		url = self.package_url(platform)

		print('Generating checksum of ' + platform + ' package (Source ' + url + ')...')
		
		return hashlib.md5( urllib.request.urlopen( self.package_url(platform) ).read() ) \
			   .hexdigest()


	def setting_to_tag(self,setting):
		"""Returns the PKGBUILD template tag corresponding to a specific setting"""

		return '<' + setting.upper() + '>' 


	def replace(self,template):
		"""Replaces the tags on the PKGBUILD template with the settings"""

		for setting in self.settings.items():
			template = template.replace( self.setting_to_tag(setting[0]) , setting[1] )

		for metadata in self.metadata.items():
			template = template.replace( self.setting_to_tag(metadata[0]) , metadata[1] )

		return template


	def execute(self,template_path,output_path):
		"""Generates a PKGBUILD from the specified template file and the current settings"""

		template_file = open(template_path, 'r')
		pkgbuild_file = open(output_path, 'w')

		template = template_file.read()
		output   = self.replace(template)
		pkgbuild_file.write(output)

		template_file.close()
		pkgbuild_file.close()


def run():
	"""Generates a PKGBUILD and a .install files with the current package settings"""

	pkgbuild_template_path = 'PKGBUILD_template' if (len(sys.argv) <= 1) else sys.argv[1]
	pkgbuild_output_path = 'PKGBUILD' if (len(sys.argv) <= 2) else sys.argv[2]
	install_template_path = 'biicode.install_template' if(len(sys.argv) <= 3) else sys.argv[3]
	install_output_path = 'biicode.install' if(len(sys.argv) <= 4) else sys.argv[4]

	g = generator()
	
	g.execute(pkgbuild_template_path,pkgbuild_output_path)
	g.execute(install_template_path,install_output_path)


if __name__ == '__main__': 
	run()
