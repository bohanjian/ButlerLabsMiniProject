"""
THIS IS NOT THE MAIN FILE. IN ORDER TO RUN THE PROGRAM, PLEASE RUN pdfExtraction.py

What this file does:
Defines a function to generate match patterns that find programming languages the subject of the resume likely knows
using spaCy tokens.
Programming languages included mostly comes from a list credited in README.md.

Additional Notes:
- There are quite a few comments on what could be improved, as this is a work in progress.
- There is more information on what this program does in README.md as well as pdfExtraction.py
"""


# Generates programming language match patterns to find programming languages likely known using spaCy tokens.
# Most languages predicted by name and variations of that name.
# Some languages are predicted using common libraries from those languages,
# as it is assumed if the subject is mentioning/using those libraries, they most likely know the language associated.
def generateProgrammingLanguageMatchPatterns(matcher):
    abap_pattern1 = [{'LOWER': 'abap'}]
    abap_pattern2 = [{'LOWER': 'advanced'},
                     {'LOWER': 'business'},
                     {'LOWER': 'application'},
                     {'LOWER': 'programming'}]
    matcher.add("ABAP", [abap_pattern1, abap_pattern2])

    actionscript_pattern = [{'LOWER': 'actionscript'}]
    matcher.add("ACTIONSCRIPT", [actionscript_pattern])

    ada_pattern = [{'TEXT': 'Ada'}]
    matcher.add("ADA", [ada_pattern])

    algol_pattern = [{'LOWER': 'algol'}]
    matcher.add("ALGOL", [algol_pattern])

    apl_pattern1 = [{'LOWER': 'apl'}]
    apl_pattern2 = [{'LOWER': 'a'},
                    {'LOWER': 'programming'},
                    {'LOWER': 'language'}]
    matcher.add("APL", [apl_pattern1, apl_pattern2])

    asp_pattern = [{'LOWER': 'asp'},
                   {'IS_PUNCT': False}]
    matcher.add("ASP", [asp_pattern])

    asp_dot_net_pattern = [{'LOWER': "asp.net"}]
    matcher.add("ASP.NET", [asp_dot_net_pattern])

    # could be improved by removing references to the other meanings of the word 'assembly'
    assembly_pattern = [{'LOWER': 'assembly'}]
    matcher.add("ASSEMBLY", [assembly_pattern])

    awk_pattern = [{'LOWER': 'awk'}]
    matcher.add("AWK", [awk_pattern])

    # could be improved by removing references to the other meanings of the word 'basic'
    basic_pattern1 = [{'LOWER': 'basic'}]
    basic_pattern2 = [{'LOWER': 'Beginners'},
                      {'LOWER': 'All'},
                      {'IS_PUNCT': True, 'OP': '?'},
                      {'LOWER': 'purpose'},
                      {'LOWER': 'symbolic'},
                      {'LOWER': 'Instruction'},
                      {'LOWER': 'Code'}]
    basic_pattern3 = [{'LOWER': 'Beginners'},
                      {'IS_PUNCT': True, 'OP': '?'},
                      {'LOWER': 'All'},
                      {'IS_PUNCT': True, 'OP': '?'},
                      {'LOWER': 'purpose'},
                      {'LOWER': 'symbolic'},
                      {'LOWER': 'Instruction'},
                      {'LOWER': 'Code'}]
    matcher.add("BASIC", [basic_pattern1, basic_pattern2, basic_pattern3])

    # could probably be improved, not sure how I would go about it
    # an instance where it could be improved: a reference to the letter c when discussing the alphabet
    c_pattern = [{'LOWER': 'c'}]
    matcher.add("C", [c_pattern])

    c_plus_plus_pattern = [{'LOWER': 'c++'}]
    matcher.add("C++", [c_plus_plus_pattern])

    c_sharp_pattern = [{'LOWER': 'c'},
                       {'TEXT': '#'}]
    matcher.add("C#", [c_sharp_pattern])

    cobol_pattern = [{'LOWER': {'IN': ['COBOL', 'Common Business Oriented Language']}}]
    matcher.add("COBOL", [cobol_pattern])

    css_pattern = [{'LOWER': {'IN': ['css', 'cascading style sheets']}}]
    matcher.add("CSS", [css_pattern])

    # could probably be improved, not sure how I would go about it
    # an instance where it could be improved: a reference to the letter d when discussing the alphabet
    d_pattern = [{'LOWER': 'd'}]
    matcher.add("D", [d_pattern])

    delphi_pattern = [{'LOWER': 'delphi'}]
    matcher.add("DELPHI", [delphi_pattern])

    dreamweaver_pattern = [{'LOWER': 'dreamweaver'}]
    matcher.add("DREAMWEAVER", [dreamweaver_pattern])

    erlang_pattern = [{'LOWER': 'erlang'}]
    matcher.add("ERLANG", [erlang_pattern])

    # could be improved by removing instances of the other meaning of 'elixir'
    elixir_pattern = [{'LOWER': 'elixir'}]
    matcher.add("ELIXIR", [elixir_pattern])

    f_sharp_pattern = [{'LOWER': 'f#'}]
    matcher.add("F#", [f_sharp_pattern])

    # Tcould be improved by removing instances of the other meaning of 'forth'
    forth_pattern = [{'LOWER': 'forth'}]
    matcher.add("FORTH", [forth_pattern])

    fortran_pattern = [{'LOWER': 'fortran'}]
    matcher.add("FORTRAN", [fortran_pattern])

    golang_pattern1 = [{'LOWER': 'golang'}]
    golang_pattern2 = [{'LOWER': 'go',
                        'POS': {'NOT_IN': ['VERB']}}]
    matcher.add("GOLANG", [golang_pattern1, golang_pattern2])

    haskell_pattern = [{'LOWER': 'haskell'}]
    matcher.add("HASKELL", [haskell_pattern])

    html_pattern1 = [{'LOWER': 'html'}]
    html_pattern2 = [{'LOWER': 'hypertext'},
                     {'LOWER': 'markup'},
                     {'LOWER': 'language'}]
    html_pattern3 = [{'LOWER': 'hypertext'},
                     {'LOWER': 'mark'},
                     {'LOWER': 'up'},
                     {'LOWER': 'language'}]
    html_pattern4 = [{'LOWER': 'hyper'},
                     {'LOWER': 'text'},
                     {'LOWER': 'markup'},
                     {'LOWER': 'language'}]
    html_pattern5 = [{'LOWER': 'hyper'},
                     {'LOWER': 'text'},
                     {'LOWER': 'mark'},
                     {'LOWER': 'up'},
                     {'LOWER': 'language'}]
    matcher.add("HTML", [html_pattern1, html_pattern2, html_pattern3, html_pattern4, html_pattern5])

    idl_pattern1 = [{'LOWER': 'idl'}]
    idl_pattern2 = [{'LOWER': 'interactive'},
                    {'LOWER': 'data'},
                    {'LOWER': 'language'}]
    matcher.add("IDL", [idl_pattern1, idl_pattern2])

    # could be improved by eliminating the other use of the word 'java'
    # I am assuming if they use a java library, they know how to use java
    java_pattern = [{'LOWER': {'IN': ['java', 'junit']}}]
    matcher.add("JAVA", [java_pattern])

    # included common libraries as well as JS libraries from the sample resumes.
    # I am assuming if they use a JS library, they know how to use JS
    js_pattern1 = [{'LOWER': {
        'IN': ['js', 'javascript', 'jquery', ' jsclient', 'reactjs', 'qunit', 'winjs', 'node', 'nodejs',
               'backbonejs']}}]
    js_pattern2 = [{'LOWER': 'backbone'},
                   {'IS_PUNCT': True, 'OP': '?'},
                   {'LOWER': 'js'}]
    js_pattern3 = [{'LOWER': 'node'},
                   {'IS_PUNCT': True, 'OP': '?'},
                   {'LOWER': 'js'}]
    matcher.add("JAVASCRIPT", [js_pattern1, js_pattern2, js_pattern3])

    json_pattern = [{'LOWER': 'json'}]
    matcher.add("JSON", [json_pattern])

    labview_pattern = [{'LOWER': 'labview'}]
    matcher.add("LABVIEW", [labview_pattern])

    # Could be improved by analyzing dependant + its own parts of speech classifications
    # to eliminate the other uses of the word 'lisp'
    # Classifies some dialects of lisp as lisp. Could improve by adding more dialects
    lisp_pattern1 = [{'LOWER': {'IN': ['lisp', 'scheme', 'maclisp']}}]
    lisp_pattern2 = [{'LOWER': 'common'},
                     {'LOWER': 'lisp'}]
    matcher.add("LISP", [lisp_pattern1, lisp_pattern2])

    # Can be improved, but for now searching for logo as a proper noun should work for most cases
    logo_pattern = [{'LOWER': 'logo'},
                    {'POS': 'PROPN'}]
    matcher.add("LOGO", [logo_pattern])

    matlab_pattern = [{'LOWER': 'matlab'}]
    matcher.add("MATLAB", [matlab_pattern])

    meta_quotes_pattern = [{'LOWER': 'metaquotes'}]
    matcher.add("METAQUOTES", [meta_quotes_pattern])

    modula_3_pattern1 = [{'LOWER': 'modula'},
                         {'IS_PUNCT': True, 'OP': '?'},
                         {'TEXT': '3'}]
    modula_3_pattern2 = [{'LOWER': 'modula3'}]
    matcher.add("MODULA-3", [modula_3_pattern1, modula_3_pattern2])

    ms_access_pattern = [{'LOWER': {'IN': ['ms', 'microsoft']}},
                         {'LOWER': 'access'}]
    matcher.add("MS ACCESS", [ms_access_pattern])

    nosql_pattern = [{'LOWER': {'IN': ['ravendb', 'noSQL']}}]
    matcher.add("NOSQL", [nosql_pattern])

    # MySQL came up so much, but based on the minimal research I did, it didn't feel right to group with SQL
    mysql_pattern = [{'LOWER': 'mysql'}]
    matcher.add("MYSQL", [mysql_pattern])

    nxt_g_pattern1 = [{'LOWER': 'nxt'},
                      {'IS_PUNCT': True, 'OP': '?'},
                      {'LOWER': 'g'}]
    nxt_g_pattern2 = [{'LOWER': 'nxtg'}]
    matcher.add("NXT-G", [nxt_g_pattern1, nxt_g_pattern2])

    obj_c_pattern1 = [{'LOWER': 'objective'},
                      {'IS_PUNCT': True, 'OP': '?'},
                      {'LOWER': 'c'}]
    obj_c_pattern2 = [{'LOWER': 'objectivec'}]
    matcher.add("OBJECTIVE C", [obj_c_pattern1, obj_c_pattern2])

    ocaml_pattern = [{'LOWER': 'ocaml'}]
    matcher.add("OCAML", [ocaml_pattern])

    # could be improved by removing references to the other meanings of the word 'pascal'
    pascal_pattern = [{'LOWER': 'pascal'}]
    matcher.add("PASCAL", [pascal_pattern])

    perl_pattern1 = [{'LOWER': 'perl'}]
    perl_pattern2 = [{'LOWER': 'perl'},
                     {'TEXT': '5'}]
    matcher.add("PERL", [perl_pattern1, perl_pattern2])

    php_pattern1 = [{'LOWER': {'IN': ['php', 'cakephp', 'codeigniter', 'laravel']}}]
    php_pattern2 = [{'TEXT': {'REGEX': "(php)(.)*[0-9]"}}]
    matcher.add("PHP", [php_pattern1])

    pl_one_pattern1 = [{'LOWER': 'pl'},
                       {'IS_PUNCT': True, 'OP': '?'},
                       {'LOWER': {'IN': ['one', '1', 'I']}}]
    pl_one_pattern2 = [{'LOWER': 'programming'},
                       {'LOWER': 'language'},
                       {'LOWER': {'IN': ['one', '1', 'I']}}]
    matcher.add("PLI", [pl_one_pattern1, pl_one_pattern2])

    postscript_pattern = [{'LOWER': 'postscript'}]
    matcher.add("POSTSCRIPT", [postscript_pattern])

    prolog_pattern = [{'LOWER': 'prolog'}]
    matcher.add("PROLOG", [prolog_pattern])

    pure_data_pattern1 = [{'LOWER': 'puredata'}]
    pure_data_pattern2 = [{'LOWER': 'pure'},
                          {'LOWER': 'data'}]
    matcher.add("PURE DATA", [pure_data_pattern1, pure_data_pattern2])

    # could be improved by adding more common libraries and account for potential reference to the snake
    python_pattern = [{'LOWER': {'IN': ['python', 'ipython', 'py', 'bpython', 'spacy', 'pytorch']}}]
    matcher.add("PYTHON", [python_pattern])

    # could probably be improved, not sure how I would go about it
    # an instance where it could be improved: a reference to the letter c when discussing the alphabet
    r_pattern = [{'LOWER': 'r'}]
    matcher.add("R", [r_pattern])

    rapid_weaver_pattern1 = [{'LOWER': 'rapid'},
                             {'LOWER': 'weaver'}]
    rapid_weaver_pattern2 = [{'LOWER': 'rapidweaver'}]
    matcher.add("RAPIDWEAVER", [rapid_weaver_pattern1, rapid_weaver_pattern2])

    rexx_pattern = [{'LOWER': 'rexx'}]
    matcher.add("REXX", [rexx_pattern])

    # not positive this accounts for all cases of references to ruby the language, not ruby on rails
    ruby_pattern = [{'LOWER': 'ruby'},
                    {'LEMMA': {'NOT_IN': ['rails', 'on rails', 'on', 'Rails']}},
                    {'LEMMA': {'NOT_IN': ['rails', 'Rails']}}]
    matcher.add("RUBY", [ruby_pattern])

    # Removed Ruby on Rails because it's not really a programming language
    """
    ruby_on_rails_pattern1 = [{'LOWER': 'rails'}]
    ruby_on_rails_pattern2 = [{'LOWER': 'on'},
                              {'LOWER': 'rails'}]
    ruby_on_rails_pattern3 = [{'LOWER': 'ruby'},
                              {'LOWER': 'on'},
                              {'LOWER': 'rails'}]
    matcher.add("RUBY ON RAILS", [ruby_on_rails_pattern1, ruby_on_rails_pattern2, ruby_on_rails_pattern3])
    """

    s_plus_pattern1 = [{'LOWER': 's'},
                       {'IS_PUNCT': True, 'OP': '?'},
                       {'LOWER': 'plus'}]
    s_plus_pattern2 = [{'LOWER': 'splus'}]
    matcher.add("SPLUS", [s_plus_pattern1, s_plus_pattern2])

    sas_pattern1 = [{'LOWER': 'sas'}]
    sas_pattern2 = [{'LOWER': 'sas'},
                    {'LOWER': 'language'}]
    matcher.add("SAS", [sas_pattern1, sas_pattern2])

    scala_pattern = [{'LOWER': 'scala'}]
    matcher.add("SCALA", [scala_pattern])

    sed_pattern = [{'LOWER': 'sed'}]
    matcher.add("SED", [sed_pattern])

    sgml_pattern1 = [{'LOWER': 'sgml'}]
    sgml_pattern2 = [{'LOWER': 'standard'},
                     {'LOWER': 'generalized'},
                     {'LOWER': 'markup'},
                     {'LOWER': 'language'}]
    matcher.add("SGML", [sgml_pattern1, sgml_pattern2])

    simula_pattern = [{'LOWER': 'simula'}]
    matcher.add("SIMULA", [simula_pattern])

    smil_pattern1 = [{'LOWER': 'smil'}]
    smil_pattern2 = [{'LOWER': 'synchronized'},
                     {'LOWER': 'multimedia'},
                     {'LOWER': 'integration'},
                     {'LOWER': 'language'}]
    matcher.add("SMIL", [smil_pattern1, smil_pattern2])

    snobol_pattern = [{'LOWER': 'snobol'}]
    matcher.add("SNOBOL", [snobol_pattern])

    sql_pattern1 = [{'LOWER': {'IN': ['sql']}}]
    sql_pattern2 = [{'LOWER': 'PL'},
                    {'IS_PUNCT': True, 'OP': '?'},
                    {'LOWER': 'sql'}]
    matcher.add("SQL", [sql_pattern1, sql_pattern2])

    plsql = [{'LOWER': 'plsql'}]
    matcher.add("PLSQL", [plsql])

    ssi_pattern1 = [{'LOWER': 'ssi'}]
    ssi_pattern2 = [{'LOWER': 'server'},
                    {'LOWER': 'side'},
                    {'LOWER': 'includes'}]
    matcher.add("SSI", [ssi_pattern1, ssi_pattern2])

    stata_pattern = [{'LOWER': 'stata'}]
    matcher.add("STATA", [stata_pattern])

    # could be improved to remove more instances of the last name 'swift' as well as the adjective
    swift_pattern = [{'LEMMA': {'NOT_IN': ['Taylor', 'taylor']}},
                     {'LOWER': 'swift'}]
    matcher.add("SWIFT", [swift_pattern])

    # could be improved by removing instances of references to the company TCL
    tcl_tk_pattern = [{'LOWER': {'IN': ['tcl', 'tk', 'tcl/tk']}}]
    matcher.add("TCL/TK", [tcl_tk_pattern])

    # As much as I love LaTeX, it's not really a programming language
    """
    latex_pattern = [{'LOWER': {'IN': ['latex', 'tex']}}]
    matcher.add("LATEX", [latex_pattern])
    """

    # could be improved by removing references to the other meaning of shell
    unix_shell_pattern1 = [{'TEXT': 'Shell'}]
    unix_shell_pattern2 = [{'LOWER': 'unix'},
                           {'LOWER': 'shell'}]
    matcher.add("UNIX SHELL", [unix_shell_pattern1, unix_shell_pattern2])

    verilog_pattern = [{'LOWER': 'verilog'}]
    matcher.add("VERILOG", [verilog_pattern])

    vhdl_pattern = [{'LOWER': 'vhdl'}]
    matcher.add("VHDL", [vhdl_pattern])

    visual_basic_pattern1 = [{'LOWER': 'visualbasic'}]
    visual_basic_pattern2 = [{'LOWER': 'visual'},
                             {'LOWER': 'basic'}]
    matcher.add("VISUAL BASIC", [visual_basic_pattern1, visual_basic_pattern2])

    visual_foxpro_pattern1 = [{'LOWER': 'vfp'}]
    visual_foxpro_pattern2 = [{'LOWER': 'visual'},
                              {'LOWER': 'foxpro'}]
    matcher.add("VISUAL FOXPRO", [visual_foxpro_pattern1, visual_foxpro_pattern2])

    vrml_pattern1 = [{'LOWER': 'vrml'}]
    vrml_pattern2 = [{'LOWER': 'virtual'},
                     {'LOWER': 'reality'},
                     {'LOWER': 'markup'},
                     {'LOWER': 'language'}]
    matcher.add("VRML", [vrml_pattern1, vrml_pattern2])

    wml_pattern1 = [{'LOWER': {'IN': ['wap', 'wml']}}]
    wml_pattern2 = [{'LOWER': 'wireless'},
                    {'LOWER': 'application'},
                    {'LOWER': 'protocol'}]
    wml_pattern3 = [{'LOWER': 'wireless'},
                    {'LOWER': 'markup'},
                    {'LOWER': 'language'}]
    matcher.add("WML/WAP", [wml_pattern1, wml_pattern2, wml_pattern3])

    xml_pattern = [{'LOWER': {'IN': ['xml', 'msxml']}}]
    matcher.add("XML", [xml_pattern])

    xsl_pattern = [{'LOWER': 'xsl'}]
    matcher.add("XSL", [xsl_pattern])
