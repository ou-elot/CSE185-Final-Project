setup(
  name = 'gwas',
  version = 0.1,
  description= 'CSE 185 S24 Final Project Gwas',
  authors = 'Elliott Ou, Lenny Lei, Audria Montalvo',
  author_emails = 'elou@ucsd.edu, wlei@ucsd.edu, ansaravi@ucsd.edu',
  packages = find_packages(),
  entry_points = {
    "console_scripts": [
      "mygwas=mygwas.mygwas:main"
    ],
  },
)
