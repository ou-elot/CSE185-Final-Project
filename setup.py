setup(
  name = 'gwas',
  version = VERSION,
  description= 'CSE 185 S24 Final Project Gwas',
  authors = 'Elliott Ou, Lenny Lei, Audria Montalvo',
  author_emails = 'elou@ucsd.edu, wlei@ucsd.edu, ansaravi@ucsd.edu',
  entry_points = {
    "console_scripts": [
      "mygwas = mygwas.mygwas:main"
    ],
  },
  install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
        'statsmodels',
  ],
)
