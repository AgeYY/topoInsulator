(TeX-add-style-hook
 "scuthesis"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("graphicx" "dvips") ("hyperref" "CJKbookmarks=true" "pdfborder=001")))
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperref")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "braket"
    "graphicx"
    "xcolor"
    "hyperref"
    "wasysym"
    "array"
    "geometry"
    "setspace"
    "fancyhdr"
    "fontspec")
   (TeX-add-symbols
    '("keyword" 1)
    '("grade" 1)
    '("id" 1)
    '("majorEng" 1)
    '("major" 1)
    '("collegeEng" 1)
    '("college" 1)
    '("adviserEng" 1)
    '("adviser" 1)
    '("authorEng" 1)
    '("titleEng" 1)
    "varTitle"
    "varTitleEng"
    "varAuthor"
    "varAuthorEng"
    "varDate"
    "varAdviser"
    "varAdviserEng"
    "varCollege"
    "varCollegeEng"
    "varMajor"
    "varMajorEng"
    "varID"
    "varGrade"
    "varKeyword"
    "makecover")
   (LaTeX-add-environments
    '("abstractEng" 1)))
 :latex)

