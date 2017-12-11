import time

asciiArt = [
    ("````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````"),
    ("````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````"),
    ("``````````````````````````````````````````````````````````````````````````````..````````````````````````````````````````````````````````````````````"),
    ("````````````````````````````````````````````````````````````````````````.``,.,:,..``````````````````````````````````````````````````````````````````"),
    ("````````````````````````````````````````````````````````````````````````+++#++:;::.`````````````````````````````````````````````````````````````````"),
    ("```````````````````````````````````````````````````````````````````..;##############';.`````````````````````````````````````````````````````````````"),
    ("```````````````````````````````````````````````````````````````````.+##################+.````````````````````````````````````````````````````````````"),
    ("``````````````````````````````````````````````````````````````````'#####################'````````````````````````````````````````````````````````````"),
    ("`````````````````````````````````````````````````````````````````'#######################;```````````````````````````````````````````````````````````"),
    ("```````````````````````````````````````````````````````````````.+#########################:``````````````````````````````````````````````````````````"),
    ("`````````````````````````````````````````````````````````````.+############################.`````````````````````````````````````````````````````````"),
    ("````````````````````````````````````````````````````````````.'##############################`````````````````````````````````````````````````````````"),
    ("````````````````````````````````````````````````````````````,###############################,````````````````````````````````````````````````````````"),
    ("```````````````````````````````````````````````````````````.#################################.```````````````````````````````````````````````````````"),
    ("```````````````````````````````````````````````````````````,##################################```````````````````````````````````````````````````````"),
    ("```````````````````````````````````````````````````````````+##################################'``````````````````````````````````````````````````````"),
    ("``````````````````````````````````````````````````````````'####################################+`````````````````````````````````````````````````````"),
    ("`````````````````````````````````````````````````````````,#######++'+'+##+++++####+#++##########.````````````````````````````````````````````````````"),
    ("````````````````````````````````````````````````````````.+###++'';:::;;'''+;;;'++#+;;+++###+####+````````````````````````````````````````````````````"),
    ("``````````````````````````````````````````````````````..;###+'';;;::,:::::::,::;;;;'::;;++#';####,```````````````````````````````````````````````````"),
    ("`````````````````````````````````````````````````````...###+';;;::::,,,,,,,,,,,,,,:,,::::;+',;####```````````````````````````````````````````````````"),
    ("`````````````````````````````````````````````````````..,###+;;;::::,,.....,,......,,,,,,,,:,,:+###.``````````````````````````````````````````````````"),
    ("```````````````````````````````````````````````````....:###';;;:::,,.................,,,,,,,,:'###```````````````````````````````````````````````````"),
    ("```````````````````````````````````````````````````...,'###;;;;::,,,........``...........,,,,:'###,``````````````````````````````````````````````````"),
    ("``````````````````````````````````````````````````...,,####;:;::,,..........``.```.......,.,,,;###.``````````````````````````````````````````````````"),
    ("``````````````````````````````````````````````````...,:+###';;:,,,.........````````.......,,,,;###:``````````````````````````````````````````````````"),
    ("`````````````````````````````````````````````````....,:####';:,,,.........`````````........,,,;###.``````````````````````````````````````````````````"),
    ("`````````````````````````````````````````````````...,,:###+;;:,,...........````.```........,,,;###,``````````````````````````````````````````````````"),
    ("`````````````````````````````````````````````````...,::###+;;:,,...........````.``..........,,:###.``````````````````````````````````````````````````"),
    ("````````````````````````````````````````````````...,,:;+##':::,.................`............,,+##```````````````````````````````````````````````````"),
    ("````````````````````````````````````````````````...,:::+##;::,,,,..........`...``.............,+##```````````````````````````````````````````````````"),
    ("```````````````````````````````````````````````....,:::'##:::,,,,,........``````..............,'#;```````````````````````````````````````````````````"),
    ("```````````````````````````````````````````````...,,:::'##::::,,''';;,....```````......,,,,,,,.'#````````````````````````````````````````````````````"),
    ("```````````````````````````````````````````````...,,:::'##::,::''';+###+',.`.....,;''+'''':,,,,'#````````````````````````````````````````````````````"),
    ("```````````````````````````````````````````````...,::::;##,::;;,,...,;###'..`..,'+###+;:,;;;,,,'#````````````````````````````````````````````````````"),
    ("```````````````````````````````````````````````...,:::.'##,,::,,,,'+'++##+;.``.:++++;,.....::..'+````````````````````````````````````````````````````"),
    ("```````````````````````````````````````````````...,:::+'+#,,,,.,;+'###'''#+,``.;'+++';'+:...,..'',```````````````````````````````````````````````````"),
    ("```````````````````````````````````````````````...,:::++'#,,.,,,'#,###.:,'+,...;,'+'#'#'';,...,'',```````````````````````````````````````````````````"),
    ("```````````````````````````````````````````````...,:::+;'#,,,.,,:+;'+',:::',..,:,+;.##':+;,...,'.:````````````````````````````````````````````````````"),
    ("```````````````````````````````````````````````...,:::':;+,,,...,,,,,,:::;;;,.,:,,:::;;;;,.....'.,````````````````````````````````````````````````````"),
    ("```````````````````````````````````````````````...,:::';+',,,.......,.,,:;;;,.,,:,::,::,.......;.,````````````````````````````````````````````````````"),
    ("```````````````````````````````````````````````...,,::;;#:,,,........,,,::'':,::,,.............;.,````````````````````````````````````````````````````"),
    ("```````````````````````````````````````````````...,::::+#:,,...........,:;';:,::,,.............;..````````````````````````````````````````````````````"),
    ("```````````````````````````````````````````````...,::::##:,,,...........:'';,,,;:......`..`....,..````````````````````````````````````````````````````"),
    ("```````````````````````````````````````````````...,::::'#',,,,..........'+';,,,:;.......`.......,.````````````````````````````````````````````````````"),
    ("```````````````````````````````````````````````..,,::;:;'#,,,,,.......`,'':,.`.,:,.............,;,````````````````````````````````````````````````````"),
    ("```````````````````````````````````````````````..,,::;,::':,::,,......`'::::.`.,,,.`..........,'..````````````````````````````````````````````````````"),
    ("```````````````````````````````````````````````...,::;;:;'::::,,.....`.+;'#+:,:#;,.`.........,,..`````````````````````````````````````````````````````"),
    ("```````````````````````````````````````````````...,::;;:'+;::,,,.......:++;;;::'':.``.......,,,..`````````````````````````````````````````````````````"),
    ("```````````````````````````````````````````````...,::;;;;';::,,,......,:;;;,,,:;:,,.``......,,,.``````````````````````````````````````````````````````"),
    ("```````````````````````````````````````````````...,::;;;;;;:,,,,.....,,:;:,..,.:::,,.`......,,,```````````````````````````````````````````````````````"),
    ("```````````````````````````````````````````````...,::;;;;;;:,,,,.....,,,,,,,::,.,,:,.`......,,````````````````````````````````````````````````````````"),
    ("```````````````````````````````````````````````...,::;;;;;;::,.,.......,,,;;:::.......`.....,,````````````````````````````````````````````````````````"),
    ("```````````````````````````````````````````````...,::;;;;;;;:,,,,.....,;+';++#';',..........,,````````````````````````````````````````````````````````"),
    ("```````````````````````````````````````````````...,::;;;;;;;:,,,,....+##++++#+#++#+;........,`````````````````````````````````````````````````````````"),
    ("```````````````````````````````````````````````...,::;;;;;;;:,,,,....,;++';:;;:;;'+;..`.....,`````````````````````````````````````````````````````````"),
    ("```````````````````````````````````````````````...,,:;;;;';;;,,,,,....,:;';::,::';,..``....,,`````````````````````````````````````````````````````````"),
    ("```````````````````````````````````````````````....,:;;;;;'';:,,,,...,,,,,:,:::,,....`..,,.,.`````````````````````````````````````````````````````````"),
    ("````````````````````````````````````````````````...,:;;;;;'';:,,,,,..,,,....,:,...........,,``````````````````````````````````````````````````````````"),
    ("````````````````````````````````````````````````...,,:;;;;;;;;:,,,,,.,,,.....,............,.``````````````````````````````````````````````````````````"),
    ("````````````````````````````````````````````````...,,:;;;;''';;,,,,,...,,,.,.,,,.........,:```````````````````````````````````````````````````````````"),
    ("````````````````````````````````````````````````...,,:;;;;;''';;:,,,,,..,,,....,,.......,:,```````````````````````````````````````````````````````````"),
    ("````````````````````````````````````````````````...,,:;;;;;'''+';;::,,,,,,..,...,......,,:,```````````````````````````````````````````````````````````"),
    ("````````````````````````````````````````````````...,,:;;;;;';'++';;;,,,,,,,.,..,,,,,,,,,,,,```````````````````````````````````````````````````````````"),
    ("````````````````````````````````````````````````...,,:;;;;;';;'++'';;;::,:,,,.,,,,,,,,,::,,```````````````````````````````````````````````````````````"),
    ("````````````````````````````````````````````````....,:;;;;;;;:;'+++';;';:::,,,,,,,::,,::,,,```````````````````````````````````````````````````````````"),
    ("````````````````````````````````````````````````....,::;;;;;:,,;''++'';';;;;::;;;;;::;;,,,.```````````````````````````````````````````````````````````"),
    ("````````````````````````````````````````````````....,::;;;'';,,,:;'+++';;;::::;:;;''';,.,,.```````````````````````````````````````````````````````````"),
    (" ````````````````````````````````````````````````...,::,'##+::.,,::''''+'';;;;''':::,,.,,:+```````````````````````````````````````````````````````````"),
    (" ````````````````````````````````````````````````...,,.:###':,,..,,:::::;;;;;:,...,,...,:;#,``````````````````````````````````````````````````````````"),
    (" ````````````````````````````````````````````````.....:;+##':,,....,,,............,...,,:'#,``````````````````````````````````````````````````````````"),
    (" ````````````````````````````````````````````````.....:,'##':,,,.....,..```````.......,,:+@.``````````````````````````````````````````````````````````"),
    (" ````````````````````````````````````````````````....,.,+##':,,.........````````......,,:+@.``````````````````````````````````````````````````````````"),
    (" ```````````````````````````````````````````````.......:###':,,.........```````........,;##..`.```````````````````````````````````````````````````````"),
    (" ```````````````````````````````````````````````.......;#++':,..........```````.......,:'#'.`..,``````````````````````````````````````````````````````"),
    (" ``````````````````````````````````````````````........'#++':,,..``.....``````.......,,;#:.##`..:.````````````````````````````````````````````````````"),
    (" ````````````````````````````````````````````..........;+++':,,..``.....``````.......,:+#,'+#@...,.``,````````````````````````````````````````````````"),
    (" ```````````````````````````````````````````..,;...`...:+++':,,..```.....`````.......,;#:`.;##@;...,.`````````````````````````````````````````````````"),
    (" ``````````````````````````````````````````...;+...#..`,+++':,...````....```........,:++...;#@#++:....````````````````````````````````````````````````"),
    (" `````````````````````````````````````````..,,';..##'.`.+++',.....```....```........,+;`..,,+@#++',.,...``````````````````````````````````````````````"),
    (" ````````````````````````````````````````..,.:+:.##@#:..++';,......``.....`........,'#.....,:#,,,,..,..`.`````````````````````````````````````````````"),
    (" ``````````````````````````````````````......:+.:##@@:..+';;:......`.....`.``......:#+.....,:#,.....,,.......`````````````````````````````````````````"),
    (" ````````````````````````````````````....`...;+.:'###;`.';:;,,.....````.`.``......,+:,,....,:+..........`......```````````````````````````````````````"),
    (" ``````````````````````````````````.`..`.....;#.:;+###..':;::......``````.````...,+.....:..,':...`....,........`.`````````````````````````````````````"),
    (" `````````````````````````````````.``.````.,.;#.:;+###;:+:;;,,.....`````````.`..,;......,``,+.........,..``.`..```.```````````````````````````````````"),
    (" ```````````````````````````````..``.````....:+'.:;+###.,,;;,.......`````.`....,,..`.`..`:,:'.`.`.`.......`......`.`.`````````````````````````````````"),
    (" `````````````````````````````..`.```..```...,++,::''##:...:,.......````.````.,'..`.......,,:..`..``...............```..``````````````````````````````"),
    (" ```````````````````````````..``.``````````.`.,''..;:+##....::,,,,..````...`..'``.```.....,,,..`..``.................```..````````````````````````````"),
    (" ``````````````````````````..```.```.`````..``.,',.,,;###;...;;;::,..`````...::``..```.......```...`...`...``.`.....``````..``````````````````````````"),
    (" ````````````````````````..`````.`..``````..```......,;+##;...:::,...`````..,+``.``.`.`.......``..`.......,.`.......`````....,````````````````````````"),
    (" ``````````````````````...`````..`..````.`..`.`........:+##,.........````...:,.````.``...`.....``.```.``...,.`.......``.......,```````````````````````"),
    (" ````````````````````....``````....```````.``.`.........:'#;......`...``...,'```````.....`.....``.....```..,.........``..,......``````````````````````"),
    (" ``````````````````....`...````....``.```.,``.`.`.``...`,;+#.`...``......,.;.`````.``..`.`....``.....````......`.,....`.`.......``````````````````````"),
    (" `````````````````.,:...```.```....``.````,`````.```.....,'#+....`........,+`.`. `.`...```...`````......`......`.......`...,.....`````````````````````"),
    (" ````````````````.,..:..``...``.``..`````..`````````...`..:++:.`.........,,;```.````...`...``.````...``..`...,..`.....``.........`````````````````````"),
    ("  ``````````````..,,.....``...`....``````..``````.``...``..:+#...........,'``````,`....`..```````.`..``.````.,..`...`..`..........````````````````````"),
    ("  `````````````..,,.,...`.`....`..```````..```````..``...`..;+#,...,.....,+````.`....```....``````.```....``..,....`...............```````````````````"),
    ("  ````````````...,.,....`.`....`..``````...```.``.```.`.``..,'##....,,.:,,:```.`.`...`...````````......`.````....```....`..........```````````````````"),
    ("  ```````````..,,,.......`.`.......````...`.``..`.``..````...,'#;..`,..,.;```.......`.`..`````````..````...```.,..``....`...........``````````````````"),
    ("  ``````````...,,,....,...``...:...```.`..````.```````````...`,+#,..`;,:,'`....`...`......``````````````.``.``.....`....``..........``````````````````"),
    ("  `````````....,:,....,`..`.``.;`..``.`...``.````````.```.````.;+#....':,;``..``..``.`...``````````.````.``````......................`````````````````"),
    ("  `````````..,,,,.....,`.......;`..``.....````.``````..``.``..`.:+#...','.`..````.``.`.`.`.```````..``...```.`........:..............`````````````````"),
    ("  ````````..,,,:,..``.,.``.....:`..`.....``````````.`.`.``.......;##...:'`..```...`....`.``.`.````.`.```.``````............`..........````````````````"),
    ("  ````````..,,,:,.....,.``..`.,:`..``.....```````````````````.....;#'..,+,,.``........`````````````..`..```..```.....,....:`..........````````````````"),
    ("  ```````..,:,,,,.....,.``..`.,,`````...`.````````````.````..`.....;+;.`',,.``..`.`..``....`.``.````.`.`.````.```..`.,....,...`........```````````````"),
    ("  ```````..,:,:,......:.``.,.`,.`````.....````````````.````.```.``..'#:.,:..```.`.....`.`.``````````......``.```.`...,...,.......`..,..```````````````"),
    ("  ``````...,:,:,......,......`;.`````.....`````````````````.``````..,'+..:,.```.``..``..```````..``..````````.``.`..`.,..'`.....`.......``````````````"),
    ("  ``````..,,::,....``..,.`.,..'.`.```..``.`.``````````````````````....'#`,:.````....```.```.````...``.`.````.`..``......,,`....`........``````````````"),
    ("  ``````..,::;,........;`..,..;`````...``.`````````.``````````..````...'+.'.`.``..`.``````````````.``..`.```.``.``.`..,.+`...............`````````````"),
    ("  ``````..,:,'..`......'``.,..'.````..```...````.`````.````.`````````...+,+.`.....`````.`````````.```.`.````.`...`.```.,'``..............`````````````"),
    ("  `````...,::;..`....`.:.`.,..#``.``.`.``...``.``..`````.`````````````..,+....`...```````````.````````.````````.`````.,'..`..............`````````````"),
    ("  `````...,:::......``..,..,..'.`.``.```.....`````..`.`.`.`.`````````..`.,,..`.````.```````````.````````..`..``...`.``,+.``....``.........````````````"),
    ("  `````..,:::,.``...`.`.'.`,..'.`...``.`....`..``......````.`````````.````,.,.`````````.`.`````....```.`...`..````.``.,:..................````````````"),
    ("  `````..,:::,``.`...``.+....:+.....`............````````...`````````.``.`..,..`..``````````````.```.`.``.`.`.```````.';:...`.............````````````"),
    ("  ````...,:::,`.``......:..,.'#.....`.....,.``````````````..```````````...+:,.`.`.``.`.```````````..````......```````.+:'......`.,........````````````"),
    ("  ````..,::;:,````..,.``.:...#+...,.....``````.````````````.`````````..`..,;,..````````````.`````..`..```.`....``````.:+,`.....`...........```````````"),
    ("  ```...,::;:,..`.`.,....'...+'.,..,....`.``.`````..```````..````````.````,:,.....```.`.```````````..```````....`.```.:+.`....``...........```````````"),
    ("  ```...,:,;,,...`......`;...+,....,....`````..````.```````..````````````.,,.,....`...`.`..`..`````.`````.```.``.`.``.;:.....```...........```````````"),
    ("  ```..,,::;:...``...,.``,:.`',...,.....````.`````..```````..`..``````````.,.,....``..`.`````.`..``.`...`........`..`.:,:....``............```````````"),
    ("  ``...,::,;:..`````.,..``+..:;...,,,....```.```.`````..```..``````````.``.,,;..`....``````.`.`.``.`..`.....`....`..`.,:,`..................``````````"),
    ("  ``...,::,;;...````.,....;...#...:.:..`.```.`````.``.`.```````````````.``.,,:...``````.``````````.```.`..`.`....``..`:#...,......,.........``````````"),
    ("  ``..,,::,:',.``.`..,..`..;..#..,,.......``````...``.``````.````````.````.,::`....````.```````.```````.`........`....;#`..,.................`````````"),
    ("  `...,,::,,:,.`.```.......'.`#:`,,.,.....`...````.``...````.`````````.`.``,::....`.``.```````````````.``...`........,+:`.,..`.........,.....`````````"),
    ("  `...,::,,,:,.``..`..,...`,,.+,.,,.......```..`...``..`````...````.``````.,,:.....``...```````````.```.............,.:...:,.``.........,....`````````"),
    ("  `...,:::,,::,.`...`..,..`.;.:,..,,,....``....`````.```````.`.````````..`.,,,........`.`````.``.`..````............,.;..,:,............,....`````````"),
    ("  `..,,:::,,,:..`..`.....`.`,..:,,,,,..........`.```.`.`````...`.``.`.`.```,.......````.``.``.`````.``......,..`..,...'...:,.............,....````````"),
    ("  `..,:::::,::,.....``.......,.::,,,,,,.`.......`.`....``.`````.``````.```.:........`.`.`````.`````.``.`..`.......,.,:+...:,,...........,,....````````"),
]

def Main():
    count = -1
    for i in range((len(asciiArt))):
        time.sleep(0.1)
        count += 1
        print (asciiArt[count])

try:
    Main() ##Call main function
except KeyboardInterrupt:
    print('__________Goodbye__________')
    pass