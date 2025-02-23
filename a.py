import random;
razasOrigen = ["humano", "gigante", "gyojin", "triton", "minks", "tonttata", "lunarian", "bucanero", "tres ojos"]
personaje = {}
zonaNacimiento=[]

def crearPersonaje():
    nombre = input("Introduce el nombre de tu personaje: ")
    personaje["nombre"] = nombre
    raza = random.choices(razasOrigen, weights = [80,5,3,2,3,2,1,2,2], k =1)[0]
    personaje["raza"] = raza
    if raza == "humano":
        personaje["arte"] = r"""
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNNXXNNNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMMWNXKK0OOOOOOOO0KXNXNWWMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWX0000000OOO000OkdodxkO0XWMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKO0OOOOOOOOO00OOxooddxkkk0NWMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXO00kOOOOOOOOOkkxocoddxkkkkOXMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWK00xddolcc:::::::;;clodxO0kxONWMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0dl:ccllllolloocc:,'',:dk000O0NMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXkol:::ccxkc,::;::cccc:cxxdOKKOkKWWMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMWNX0Okxdc.. 'cokKk:;dc;,....:dxxdoddxkO00KXKXWMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMWNK0kdddoc....lxxk0K0xkOxdl'...cdoxxdlcdkOOOklcdxdkNMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMN0kxooool;;;:O0OO0O0K00OOO:,::coooodk0X0xdO0Oxl;',lKWMM
MMMMMMMMMMMMMMMMMMMMMMMMMMWNX0OkxdllclOKKKKKOO0000xccddxkO0XNWMMKl,cdkkol:,,lKWW
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNNX0dd0K0OOOkOOOxox0NWWWMMMMMMMNkc;;co:',,;;:dK
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0xdkkkkkxxoo0WMMMMMMMMMMMMWk:;;,;;,',,,;;d
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXOOOxodddoOWMMMWWMMMMMMMMWN0kc,''''',,,;d
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNK0XX0OKKK0OOkddddk00Okk0KKK0Okdoc;,,,,'..,:kN
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN0kdccx00OO0KKK0xdoc:,,;;:;;;:::;;;;;;;,,,cox0XWM
MMMMMMMMMMMMMMMMMMMMMMMMMMWWN0ko:;:cok00OOk000Okkkdc,,;;;;,,;;;,,,,,;cdk0NWWWMMM
MMMMMMMMMMMMMMMMMMMMMMMMWWKOdlc:;,,:okKKKK00KKKKKOo:',;;;,,,,,''':ok0NWMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMWKolc;;;;;,,:dOKKKK00KKK0xc,,;;,''''.,cdOXWMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMM0l:;;;;;;,;;:okOO0OO00Odl:,,;,''..;o0NWMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMM0l:;;;;;;,:l:cdxxkkxkxdoc:;;;'''.;OWWMWWMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMWOc:;;;;;;;;;;lxxddooddddc:;;;,''.lXMMMWMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMXd:;;,';:;;cl:lolodxxxdolc:;;;;,''dWMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMM0l;,;,',:;;cl:lddxOOOkxdoc:;;;;;';OMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMNd:;,,;,';;;;;;oOO000kOOkdc:;;;;;';0MMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMWOc;;,''',;;:l::dkOOOkxkOOxl::;;;;',OMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMXo:;;,',,,;;:c;cOKKKK0OKKK0kl;;;;;,'xWMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMNk:;;;';dl;;;;;;lOKKK0Ok0KKKKkc:;,;,'cKMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMKl;;,,,dOc;:;:lc:oxxkOkxOOOOkxolc;,'''xWWWMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMWk:;;,'cOx:cc:;::;:dk0K00KK0kxOkol:;,'.:0WWMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMWWKl;;;,,xkc::;;c:;:cxKKK00KKKKkk0xoc,''.':kNMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMW0o:;;,'cxl:,'',ododOKKKK00KKKK0kOK0x;'..'',oXMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMWKxc:::;''coc;'',:dkO0KKKKKKKKKKKK00KKk;'''''''c0MMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMWOl;;;;;,'',;;''cddxO000000K00000OkO00Oxl,.''''''dWWWMMMMMMMMMMMM
MMMMMMMMMMMMMMM0:,,'.'c:'';;,;oxkkkkkOO000OOOOOkxdk0OxkOd:'''''':xXWWMMMMMMMMMMM
MMMMMMMMMMMMMMMNx;';:cl;'';,,d0OOOOOOOOOkkkkkO0OkdxO0kkOko,.''''''c0WMMMMMMMMMMM
MMMMMMMMMMMMMMMNd,'o00xc'''',d0OOkkkkxxxxxkOOkkkkxxO0kxOOd;'''''.''oNMMMMMMMMMMM
MMMMMMMMMMMMMMMWKOdxKKk:::,'cOK0OkkkkOOOOOOkkkOOOxdk0Odxkxl'''';lldKWWMMMMMMMMMM
MMMMMMMMMMMMMMMMMMX0KKkOx;',d0OkkkOOOkxxxxkkkkxddood00xodxd;''.,xWWMWWMMMMMMMMMM
MMMMMMMMMMMMMMMMMMX0X0KN0ooloddooolooddxkkkOkxdoolllx0OddddodkxxKMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMXKX00NMWNOc;;;,,,,,,;;;:ccc:,'',,,,ckOxdddkKWMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMWXKKK00KNKoc::c::;;,,,,;;:;,'..',,;;;:lxxddoxKWMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMX0KKK00OKKdc:c:::;;;,,;;;:;;,,,,:c:::::;coddoxKWMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMWKOkOKxodxkoc:::::;;;,,;;:::,''',,;::::::;,;loodONMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMN0kkO0kod0klcc:::::;;;;,',,,;;,'',;:::::::;,,:oood0WMMMMMMMMMMMM
MMMMMMMMMMMMMMMMWNKOkxkOKKdc::::::::::,......'''',;:::::::::,;oddodkKWMMMMMMMMMM
MMMMMMMMMMMMMMMMWMMWWNWMWOlc:c:::::::,'.....'....',;:::::::::cooddxxO0XWMMMMMMMM
"""
        personaje["hp"] = random.randint(80,120)
        personaje["atq"] = random.randint(10,20)
        personaje["def"] = random.randint(10,20)
        personaje["vel"] = random.randint(10,20)
        personaje["esperanzaVida"] = random.randint(70,100)
        zonaNacimiento = ["East Blue", "West Blue", "North Blue", "South Blue", "Grand Line", "Red Line"]
        personaje["nacimiento"] = islaNacimiento()
    elif raza == "gigante":
        personaje["arte"] = r"""
MMMMMMMMMMMMMMMMMMMMMMMMMMWX0OKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMNOo:cxkOXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMWKx:,:c:o0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMXd:',,';:kXKNWWNKOO0NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMW0occ;,;'.,;,,:cc;...;d0KK0Okk0NMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMXl;::;;;''....       .......'ckKNWMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMXl;::;:;'.'',;;;;,'...     ....'lkXWMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMWXl,;;:ll:',;:odxxdooc::,'.........':ox0NMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMWKo'':;,;c,.,cc:clodddooodolc:::cc;..  .':lxKWMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMWKd;,ll;'','':odoc:cooddooddxdddodddo:..   .lKWMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMNx,'cdo;'.';:loooddddddddddxxdddddddddl'.  ..;lkKWMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMNKx::lodocclloodddxxdddxddddxdl::clodxddc.      ..:dKWMMMMM
MMMMMMMMMMMMMMMMMMMNOdllolcldoloddddxdddddddddddxdc;;:llodddxl.       .'lONWMMMM
MMMMMMMMMMMMMMMMMWKxodddodddddollodddddddddddxxddl;,:lddddoloc'..    . .oNMMMMMM
MMMMMMMMMMMMMMMMMXxddddddddddddocodddxddddddooll:;,,,coddddl:clc'.     .,OWMMMMM
MMMMMMMMMMMMMMMMMKxdxdodxddddddl::cllllccccc:;;;:cc;,:odddddddddo;.     .'dXWMMM
MMMMMMMMMMMMMMMMMNOdxocldddddoc;;;;;;;,,,,;;:cclddl;,:odxxddddddxo;.   ....,oONW
MMMMMMMMMMMMMMMMMMNkdl;;:cccc:;cloooollc::clodxddo:,,;lddddoldddddl.   ..:oddkKW
MMMMMMMMMMMMMMMMMMNkdoc;:looc:lddoodddxddddddddol:;:;,;ldddlcddddxl'   .,oONMMMM
MMMMMMMMMMMMMMMMMMKxdoc;;lddooddc;::cloodddddlc:clol:,,;cll::lddddl'.   .lKWMMMM
MMMMMMMMMMMMMMMMMMKxxl::::lddddlcllooooooodollloddl:;cxd;,'',,,;:clc,.  .'dXWMMM
MMMMMMMMMMMMMMMMWNOddocol::ldooodollodddddddoloddoc:;dOl'.',;;;;,''',..  .lKWMMM
MMMMMMMMMMMMMWKxl;,,,;:cc;;:lolodl::cloooodddl:codoc:dc':lddxxxxdoc'......;oXMMM
MMMMMMMMMMMMMKo;:::::;,'..'oklldddolloddddddxdolddc;:doclccccccclol;,....ck0XWMM
MMMMMMWNKOOOOxoddxxxxxdo:..,ododddocccloodddxxddoc;..,,'''.....'''''','.'xNWMMMM
MMMMNOl;'...,;;;:::cclddl;'.:l:llooooooooooll:;'.......'',,,,''.......'';OMMMMMM
MMNOc...............'',;,,,:d:...'',:ldddo:'.........,cloddddooc:'.....,xWMMMMMM
MNx,...','.''',,,''........:l,......ckOOOxc......  .,oxxxxxxxxxxd:'.....dWMMMMMM
Wk;...';;;coodddddooc;'..............,,,,'..   ... .colcccccloddl;,,,...cXMMMMMM
Xl....,;:ldooddddxxxxdc'......''....   .....   .....;,'','.'',;;,,,,,'..oNMMMMMM
Kc....',,;;;;;;;:clodo:,.....,;'...... .....  .....''........,'....',,,lKMMMMMMM
No'....''...'..',,',;,,''...;;,....','.......','....................'cOWMMMMMMMM
M0:......';;::;'.......;llcloc'....,;:c,.....,;,,;,':odl:::,'........dWMMMMMMMMM
MWOc....;lodddxd:,,...:dddddol;''',:o0Xkooo:,;;:clcdOOxdxko::;'.....'kMMMMMMMMMM
MMMXd,.';;;;;;:okkkdccdddooolc;;;cd0NMMMMMMKo:;;;,ckOxdkOkddl;;;....;0MMMMMMMMMM
MMMMWKxc;;,,,,,;clododxdoolc:;:lxKWMMMMMMMMMNk:,,':dxdkOkdxkl:;;,.'cOWMMMMMMMMMM
MMMMMNx:;;;,,,;,,,,,cdxdoc:;:d0NMMMMMMMMMMMMMWx,.';cokOkdxxl::;:okKWMMMMMMMMMMMM
MMMMMWx:;;;,,;;;;;,,:llc;;;;:dKWMMMMMMMMMMMMMMXl''.':looooc::;;lKMMMMMMMMMMMMMMM
MMMMMMN0kkxl:::;;;;:xOc,,;;;;;cxXMMMMMMMMMMMMMWKl'...',,;;;;;;lOWMMMMMMMMMMMMMMM
MMMMMMMMMMWNXK0kO00KWWk:;;;;;;;;dXMMMMMMMMMMMMMMNk;......'';lxKWMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMNd:;,,;;;':0MMMMMMMMMMMMMMMWx;,,;::cxKNMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMXl''''...,0MMMMMMMMMMMMMMMMO;',:l:lKMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMM0c......;KMMMMMMMMMMMMMMMMXc.....xWMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMXo.....cXMMMMMMMMMMMMMMMMWk'...cXMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMNk,...oNMMMMMMMMMMMMMMMMMXc..,OMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMWk'..dWMMMMMMMMMMMMMMMMMNo..:KMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMWk'..dWMMMMMMMMMMMMMMMMMX:...lXWMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMWXkl'...cXMMMMMMMMMMMMMMMMWO'....:OWMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMW0o;...',,lKMMMMMMMMMMMMMMMMNo......;kWMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMWXOkxxO0KKNWMMMMMMMMMMMMMMMMW0kxxxxkOXWMMMMMMMMMMMMMMMMMMM
"""
        personaje["hp"] = random.randint(200,300)
        personaje["atq"] = random.randint(30,50)
        personaje["def"] = random.randint(40,60)
        personaje["vel"] = random.randint(5,10)
        personaje["esperanzaVida"] = random.randint(300,500)
        zonaNacimiento = ["Elbaf"]
        personaje["nacimiento"] = islaNacimiento()
    elif raza == "gyojin":
        personaje["arte"] = r"""
MMMMMMMMMMMMMMMMMMMMMMMMMMNk::dXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMO,...xMMMMMMMMWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMKl;',okO00kONNXXNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMWKdlc,'...'...::;;lO0KKXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMN0xcoxo:;;;cl:;,'........;okKWMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMWNXXK000KNWMMWxcdxkkkkkkkOOOkkdol:'.   ...;OWMMMMMMMMMMMMMMMMMMMMMMMMMM
MMWXKOxdc;'......';ldxocdOkxkOOKKOkkOOOOOOOd,.....  .lXMMMMMMMMMMMMMMMMMMMMMMMMM
MMN0dc,'.        ......lOOkkkkO0OOOOOOOO0Oo,..........oNMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMWN0d,.     ....'okkOkc'ckOOOOOOOOxo:......      'dOOKWMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMNd.     ..,dOOOOkdldOOOOOOkdc'....      ........':ok0KNMMMMMMMMMMMMMMM
MMMMMMMMMMMNc   .'.'oOOOOOOOOOOOOOOkd;..      ...........  ....':oONWMMMMMMMMMMM
MMMMMMMMMMMMO' .l;.:xkOOOOOOOOOOkkkkxdddol:;'.............       ..,ckNMMMMMMMMM
MMMMMMMMMMWMX;.dOc'lkkkOkkkkkkkkxxxxdd0KKKKKOkdl:,.............   ....;dOXWMMMMM
MMMMMMMMWMMMXcc0ko:ldkxxxdxkkkxxxd:cdxkOKKK000KK0kdollc:;,....,c:.    ...;dXMMMM
MMMMMMWWWMMMXddOko;;clcclcloxxxo:;,;cclOXKK0O00KKKKKKK0Oxdl:'..'okc      ..:kNMM
MMMMWXOxkKWMKddxxl;;:lllllcoxxdoccdkO00KXKKK0kkkkOKKKOdllooodo:'.',.        .c0W
MMMMXkxxdxOKxoxkkxdoc:;;:coodxOKK0KKKK00XKKKKOd:;lkOOOkkOOOkxodxl:;.          ;0
MMMWOdkkkkxld0Okkxxxl;,,,;;;d0KK0K0xk00000KKKKx,.lkkO0KKOxolooxxdxxdo;..      .k
MMMWX0kxxxockKxllooollc;:lodOKK0kO0c:OkolkKKKK0d:cdokK000OOOOkkkxl'.,:;'....  .d
WWMMMMWXK0kxxxc'';coxxdxOKXXKKK0d:lc:l::dxkOKKK0ko;:x0OOOkkxxddxxl.        ...'O
MMMMMMMMMMMOdxdo;;oxddOOOKKKKK0xl::colcclld0KKKO0O:,llc:;,;oxkkkkkc.        'oKW
MMMMMMMMMMWxlOKOddddxdkloOxOKKKKOkkO0OOO00KKKKKkllc:,...  .,oxkOOOk:      .;kWMM
MMMMMMMMMMNd;oxlclxkdc::cclk00O0KKKKKKKK0KKKKKkoc;cc,.      .cxOOOOkc. ..,dXWMMM
MMMMMMMMMMXd;;:;:d0kocoolccoxxxOKKK0xOKKKK0KKK0dloxxd;.      .ckOOOOko;..;KWMMMM
MMMMMMMMMMKc...'lkOOOOOOOkkOOOOOdx0d,oOxodk0O000KK000d;......ckOOOkkkko' ,KMMMMM
MMMMMMMMWMNk,...;lodxxxxkkkkkkxdl,:;':;;cdkdxxxxOOOkxxdoc'..lkxxkOkkkkkd',0MMMMM
MMMMMMMMMMW0:',;:col::,,ccloodc,,,,;;,',:;,coolllc:;;:::.  .oOocxxdxdodo,;0MMMMM
MMMMMMMMMMXl.:l:;::;;:;'''',,;;,,,;;;;,',,:c:::;;;,',:c:.  .lkxclollcc;. 'OMMMMM
MMMMMMMMMWO;.,,',;,,colc;;:cccclllllc;:cl::c::oolddodxdoldO00xo:;:;''..  '0MMMMM
MMMMMMMMMNd'''.;ll:;c:;c:cdddxkOOxl::,,:c:::,;:cd000OOxooONWWN0kkxd;.    :XMMMMM
MMMMMMMMW0:',:;colllc;ok;'oxxk0000OdlloddxkxxddO00000xoc:ckNWMMMMMMNk'   dMMMMMM
MMMMMMMMXo;;lo:colloo;':,'dd:xK00KKKKKKKK00KK0K0KKKK0xl:lclKWMMMMMMMW0, .OMMMMMM
MMMMMMMWx,,;::,:oocll;....,..odxOO0000KKKK0O0KKKKKKKKKOOkkOOXMMMMMMMMM0;cXMMMMMM
MMMMMMMWo',::,;ldc:co:,;;:,.',:xOO000OO00K0c:kK0dd0XKKK0000O0WMMMMMMMMMXKWMMMMMM
MMMMMMMWx';doc::cccccllloooddxkkkkkkkxl:cldc.:d:;okxOKKK000xx0NMMMMMMMMMMMMMMMMM
MMMMMMMMWOccxkkdc:coollooolooodxkOOOkoc,'',::::,;;:oO00Oxxkc'lKMMMMMMMMMMMMMMMMM
MMMMMMMMMWO;;odkOxolclollc:cddollooddocccldkOkOOkk0K0000d:;'.:0MMMMMMMMMMMMMMMMM
MMMMMMMMMWNk:,codxkOd,'co; .lxocx000OkkkxxkkkkkkkOOOOO00Od:,;coKMMMMMMMMMMMMMMMM
MMMMMMMMMXxdc.':cloooc,.',..c;.:ddk00KKKKKKK0xk0OOOkkkkkxo::cclOMMMMMMMMMMMMMMMM
MMMMMMMMMXOOOdodoclddolc:cc:,..',oO0KKK00KKKx;oKKkdOKKK00Okdoc;oNMMMMMMMMMMMMMMM
MMMMMMMMMMMMWNXNWXkolodxxxxxdoc:lxkkkOkl;:lxc.cd:;dOO0KKK0Okdl,:0MMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMN0xolloddxkkxxxxxdol:,. ......',,lkkkkxdo;,lONMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMNKkdlc:ccccccc:,',:::clolol;:ldddddxddx0WMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMWWXK00Okxxk0KKXNNWMMMMNkccccclld0NWMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNx:;:::;,,'lXMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0oodddddooclKMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0xxddooooooxKMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNNXXXKKKK0KNMMMMMMMMMMMMMMMMMMMMM
"""
        personaje["hp"] = random.randint(100,150)
        personaje["atq"] = random.randint(15,25)
        personaje["def"] = random.randint(15,25)
        personaje["vel"] = random.randint(15,25)
        personaje["esperanzaVida"] = random.randint(100,150)
        zonaNacimiento = ["Isla Gyojin"]
        personaje["nacimiento"] = islaNacimiento()
    elif raza == "triton":
        personaje["arte"] = r"""
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXNMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWMX0NWMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXKNKXNXNMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKKKKNKKWMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXKKOKXOXMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0X0kNXx0MMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMWNWWNXXNWWWWMWWMMMMWX00NXk0WXxOWMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMWX0OO00O00OkOXWWWMMMMKkOXWOkNMNxkWMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMWX000kxO000kkxkXWWMWMWXkx0KdxNWOlkWMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMWKO0XX0kxk0NKdlkNMMMWWN0doolcoxxkXMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMNOdkXX0kkkKXklckNMMWXX0xddlcodkXWMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMWXOxk0OkxkOxc:dXWMWKOOxdkkllkOOXWMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMWXkoddddxo::xNWMMWX0kkxdo:okk0O0WMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMWNK0KN0occlolc;cOXXXNNWKkOOxl:xOkkx0WMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMWXKKK0xoooddodxxxdxxooodddxkxoodocxK0O0XWMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMNOdoooooodxdooxxlcokxooxkxxdolllol:oOKWWMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMWWMMWW0dddlokO0Okxdddddodddddk0KXXK0kdxdloxKWWWWMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMWWWX0000OddxO0XKOddddddddddddddddxk0XXX0kdoookKKKNWWMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMNOdoooldk0XNXKkddddddddddddddddddox0KXOokKOxooddx0NMMMWMMMMMMMMMMMMMMMMMM
MMMMMMNOdollookKXXXXkoddddddddddddddddddoddOKxdKX0OdcooldXWWMMMMMMMMMMMMMMMMMMMM
MMMMMWNOdlloc:dKNXXKxoddoodddddooooddddocloxOdkXX0xooddod0NMMMMMMMMMMMMMMMMMMMMM
MMMWN0OOxcdkll0NXXXXkdddoooodddooooollllcllddd0NXXOodOocllOWMMMMMMMMMMMMMMMMMMMM
MMWWKdooloolokKXXXXX0ddoloolloollolllllccllookXXXX0xllddlcOWMMMMMMMMMMMMMMMMMMMM
MWWW0dllxdlOXXXXXXXXKkdolllllllllllcllccllooo0XXXXXXKklooo0WMMWMMMMMMMMMMMMMMMMM
WWWKdllloOKXXXXXXKKKKOxolcccccllllccclccodxldKKKXXXXXXKdcxXMMMMMMMMMMMMMMMMMMMMM
WWXkolx0k0XXXXK00000OOOkdollllodddddlldkOkdlkKKKXXXXXXX000KWMMMMMMMMMMMMMMMMMMMM
WWNOolOXXXXXXX0kOO00000000000KKXXXXKdcoOK000XXXXXXXXXXXXXK0NWWMMMMMMMMMMMMMMMMMM
WWNXKkOXXXXXXXK0OO0KXXXXXXXXXXXXXXK0kxOKXXXXXXXXXXXXXXXXXK0NMMMMMMMMMMMMMMMMMMMM
MNkdxdkXXXXXXXXXXXXXXXXXXXXXXXXK0OkOKXXXXXXXXXXXXXXXXXXXK0KNXKKKKNWMMMMMMMMMMMMM
W0ooocd0KKKKKKXXXXXXXXXXXXXK000kxk0KKXXXXXXXXXXXXXXXXXXK0O0OxxkxkkKWMMMMMMMMMMMM
XxlllllldkOOOO00KKXK00KK00OkxxddxkkkOO0KKKKKKXXXKK0OOOOxx00kddxxkxdKWMMMMMMMMMMM
N0dcccllloodxkkkkOOkkkkkkxxxddxxddxxxxxkkkkOkkkOOOOxdoookNXkddxxxdoxXWWWMMMMMMMM
MWKxlccccccloddxxkxddxxxxxddxdxkxdxxdolodxxxxdoodoolcox0NMNkodxxdoloOK0kO00XNWWW
MMWX0xodxolllcclllldkkkkkxxkkxxkkkkxxdcokkkkkxlllcclo0NWWMXdodddollllodxxxkkkONW
MMMMWNNWNOdlccccclloOKKKK0OOOOOKK000kddO00KKklcccclldKWWMW0ooollcclloxxxxxdddd0M
MMMMMMMMMWN0kdollllcdKXXK000KK0KK0K0xokKKKXOolllolloONWWMXxlollccllldxxxdooddd0W
MMMMMMMMMMMMN0dolddccOXXXXKKXKKKK00OoxKXXX0ocld0XK0XWMMMWKollc::clcoddxooodxkkON
MMMMMMMMMMMMMNXK0XXOxkKKXXXXXXXXXKKkdOXXXKkkOOXWMMMMMMMMWKoll:,;cclooolld0XNWWWM
MMMMMMMMMMMMMMMMWWWN0k0KKKKKKKKKKK0dxKK000OKWWWMMMMMMMMMMKdll;,:::lllloONMMMMMMM
MMMMMMMMMMMMMMMMMMMWXxoxO0000000K0kok0kxdx0NWWMMMMMMMMMMMXkl:,,,;:::lkXWWMMMMMMM
MMMMMMMMMMMMMMMMMMMMWx,,;:ccclooodocll;cd0WMMMMMMMMMWXK0KX0l,,'';:lkXWWWMMMMMMMM
MMMMMMMMMMMMMMMMMMMMKc'........',cc,,,,dXNMMMMMMMWWXOxdxx0k;,,,oO0NWWMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMNd,'.......'';l;,,,c0MMMMMMMMMW0xdoodxo:,;';0MMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMNk;'''.....'',cc;,,,oNMMMMMMMMMKdolcloc;;;,,dNMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMWWKo;'..'''''',,:l:,,,,c0WWMMMWWMWOlc:;::;,;,';0MMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMNk:,'''...'.',,,cc;,,,,,lkKWMMMMMNd;,'.',,;,,'dNMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMN0o;'''.....'.',,;c:,;,'.',,oXWWMMW0c,''.',;,,':0MMMMMMMMMMMMMMMMMM
MMMMMMMMMMMWKdc;'.,,'..'.''',,:c,,;,''.',;lkKNXOc;,'',,,,,',kWMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMKoll;,;;,'...'''',;c;,;,,,;;;;:cccl:;,,,,,;;,'',xNMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMNkdolc:co;....'''',:c,;;,,,,:llllooc;,,,,;,,''.,kNWWMMMMMMMMMMMMMMMMMM
MMMMMMMMMMXkoooloOXx,''''''',::,,;;,,,,cloddxo:,,,,'''.'c0WWMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMXxdddOXWMNd,.'....;:,',,,,,,,,,;:cdd:'''...':xNMMWMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMWWK0KNWMMWWXd,....':;.'''',,,,,'''';:,',,,;lkXWMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMWWWWNKOkdo:'....,:,''..'''''''''...',;ccldxk0XWMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMW0dlllc:;,';ccllc:'''..'',,,;:c:,',;::cc:cldKWMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMWXOkxddddxk0Xd,dWX00OOO000KKXNWN0kxxxxkkkOKXWMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMWWWWWMMMKc;0WWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMWKXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
"""
        personaje["hp"] = random.randint(90,140)
        personaje["atq"] = random.randint(12,22)
        personaje["def"] = random.randint(12,22)
        personaje["vel"] = random.randint(15,25)
        personaje["esperanzaVida"] = random.randint(100,150)
        zonaNacimiento = ["Isla Gyojin"]
        personaje["nacimiento"] = islaNacimiento()
    elif raza == "mink":
        personaje["arte"] = r"""
MMMMMMMMMMMMMMMMMMMMWMWWWWWWNXKK00OOOOkkkOOO000KKXNWWWWMMMMMMMMMMMMMWMMMMMMMWXXK
MMMMMMMMMMMMMMMMMMMMMMWNXKOkkxdxxxxxxddO0OxdxddddxxkO0KXNWMWMMMMMMMMWMMMMMMMWXXK
MMMMMMMMMWNXKNWMMMMMWX0kxxxxxkxdxxxxxxdkkkxdxxxxxdkOxddxkOKNWWMMMWXOkOKWMMMMWXXX
MMMMMMMMWOoold0NMMNKkxdxxxxdxOkxxdddxxkkOkxxxdddxxkOkdxxxxdxOKNWW0olollkNMMMWXXX
MMMMMMWKxlcolloxKKkdxxddddxxxddxkO0000000000000Okxdddxxxxddxxdk0kolllllldKMMWNXK
MMMWNKKklllcllolloxxxdx0kdxddkKK0OOkxxxxxxxxxkO0XX0kxdxxdkOxxxdlllllcllld0KXWWNN
WNKkolokOdllcclolldxxdxkxddkXN0xddxxxxkkkkxkkkxdxOKNKxdxdxkdddllollcllok0xloxOXW
Nkl:colxNKxllccoolldxxxxdx0NXxdxxOXXKOkxxxxxOKX0kxx0NNOdxxddxllolccllo0W0ollccoK
KocclolxXMXxllclolloddxxd0WXxxxdkXWMMWN0OOKNWMMMXkxx0WNOdxxxoclolcllo0WM0olocclk
kcccclloKWMKolccolclkkddkNNkdkkxxxOKWMMWWWMMMWN0OxxxxKMXxddxocllccllkWMWOlolccco
kcccclolxXWWkllcll:lkOdd0WKxxkxxkxxONMMMMMMMMXxdxkkxd0MNkddOklllcllckWW0ollcccco
Ko:ccclold0Xkllcoc:odddxKMKxxxxxxOXWMMWNXNWMMWXOxxkxd0MXxdxdolllcll:oKkollccccck
W0occcclllllllllc:lxxxxd0WXkxkxd0WWWWKOxxxOKWMWNOdkdxXW0ddxxdccllloccllllccc:cxN
MWKdlcccloolool::oxxxxxxxXWKxxxxkk00xodxxddox00kxxxxKWXkdxddo:::lllllollc:;;cONM
MMMN0dlclollc:;;coolodkOdxXWXOxddddxxkkkxkkxxdodxdkXWXkdxkd:;:llcc:::::;,;lxXWWW
MMMMMNKOxxdddlcclll:;coddddkOOxdxkxxkkkkkkkxkkkxddk0kollll:,;lxxc;;oxddxk0NMMMMM
MMMMMMMMWWWWW0dolllc:::clooddxxkkkxxdooooodxxkkxxkxdolc:;:::cc::;;dNMMMMMMMMMMMM
MMMMMMMMMMMMMNOlldkOOoldxkkxxxxxdolloodxxddooodxxkxxxkxoc;:x0Oxl:dXMMMMMMMMMMMMM
MMMMMMMMMMMMMMNkoooddoxkxkkxdollodxkO000000OOkdoooodxxxooc:lolcckXMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMN0xxxxdodddxddxxxkO000000000000Okxdooolccc:;::;l0WMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMWXkddxdolx0Od:,,okO00000K0000Ox:',ckOko:;;;;lkXWMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMWN0oldolk0ko;..:xO00xc:::d00Od;.'ck00xllc;dXWMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMM0ddc:cllxK0OOkkOO000kocclx00OOOOOO000dlodkNWMMWMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMNd;,;:::cdO00000K0OkOxlccoxkkO000K000xolokNMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMXdlloocolx0kk0000000kc;cc:lkO0000OkxkOxoo0WWMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMWkloxxdddkXKKK0xdddxxddkkxxkxddk00KXWNkodKWWMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMNOxkxxddkOOOOkl;;;;;codxdl:,,,cKMMWMWkddONWMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMWMMWXkdoxNWNNKl,;:lxo:cllcldl;;;oXMWWXOxod0NMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMXxod0WWMWO:,:oOXOdkOkxxXKo:;:d0NWN0OkkONMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMKxxKWMMW0l;;okXKkkKNKOx0XOo;,;cxKNK000KNMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMWNNWMMMXo;;lk0N0xOXNKOkOXKkdl::dxk0XNWWMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMWO::lxkKNOkOXNXOkkKW0xxo:dOkkO0XWMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMWxcdkkkXXOkOXWXOkk0WXOkxclKOkkooKMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMkdkkxkKOxdxKXKkxkkKKkdxooXNkc;:OMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMKdddxk0xoox0KKkdxxO0xodlxNMWKxd0MMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMNkloooollodxxxddddddooccOWMMMWWMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMNkodddddddddddddddddl:xWMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMKdodddddddddddddool:dXMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMNkoddolcldxxdllcc:;c0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0olloox0NWWNOd:;;;dNMWWMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMWMWMNkdokXWMMMMMWWOoodXMWWMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMWMN0kOOOkkXMMMMMMMMMXOOkOKXWMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMNOo:;clxOk0WMMMMWMMW0OOoc::d0WMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMM0l;;:c:ck0KWMMMMMMMN0kl;::;;lKMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMWKOkkOO0XNMMMMMMMMMMWKkdoodk0XMMMMMMMMMMMMMMMMMMMMMMMMMM
"""
        personaje["hp"] = random.randint(100,160)
        personaje["atq"] = random.randint(18,28)
        personaje["def"] = random.randint(12,22)
        personaje["vel"] = random.randint(25,35)
        personaje["esperanzaVida"] = random.randint(90,140)
        zonaNacimiento = ["Zou"]
        personaje["nacimiento"] = islaNacimiento()
    elif raza == "tonttata":
        personaje["arte"] = r"""
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMWXK0OOOOXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMWNXkolllooxXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMWK00kdoc:cco0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMXOkdk0xc:;:ox0NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMWXOxxkkkdlcodkOONMMMWX0XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMNOdONKkoloxxxKMMWKxookNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMWKO0NKkoodddkXMXkxkdldXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMN00XKkoodxxkX0xkkkxldNMMMMMMNklOWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMN00KOo;cxOxxxxkkkkxlxNMMMW0c. :KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMX0OKNWMMMMMMWKOd, .;xkdxkkkkkkdlkWMNx.   ,OWNKKNMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMM0olddkOXWMMMMW0:.   'cdkOOOkkkkdcoxc.    .dOkxddKMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMWKddxxddxOKNWNx.     .ok0K0Okkkxo'.      'oxxxxdd0WMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMNkdxkkxddxkkc.     ;xkO0OOkkkkxl;.   .:dxxoccllo0WMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMNkdxkOOOkxdl,.   .lkkO0Okkkkkkxdl,,cdxxxxdc;,;coONMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMNkoxO00Okkkxdc;':dkkOOOOkkkkkkkxxkkkxxxxdl:,;lolxXMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMNkdxkkxxkkkkkkxkkkkOOOOOkkkkkkkkkkkxxdddoc;oKKxlo0WMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMXxoxxdxkkkkkkkkkkkOO0OOkkkkkkkkkkxxxddol:cOWMWKxxKMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMKocldxkkkkkkxxxxkkOOOkkkkxxxxxxxxxddoc;,oNMMMMWWWMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMNd:oxkkkkkxdxxxxkkkOOkkxkkocc:ldxdddl;,;kMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMWOldxkkkxddl::;;:okxdooxx:,;'..'oxool:,cKMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMXdoxxxxddo'':,...dxcc:dl.,:,...;oclc:;oXMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMWkcllol:ld;.'...'odclloo:''...,cc;,;;;oNMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMKl;::cllll:;,;:okOKKK0kdlcc:cc;;ll:;;xWMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMWx;:lddc;ldxxkOOKXXXXXXKOOOOOkl,,:llckWMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMM0oooc;:dKXXXXXXXXXXXXXXXXXX0Oxc,,,;:ckWMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMWKxl:;;coOKOOKXXXKO0K0KKXKK00Okkoccc;,;lXMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMXo::lldxdOK0OxdkOOdxOdxkkOOddK0OdoxkocookNMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMNkolxxoOOdkK00kxxxkOK0xxkkOOO0KOkxxOkdddxOXMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMNkdodOxldkod0O0KK0KKKK0OOKKKKKK00kdddooodOXWMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMWW0occcddlcllcdKXXXX0o:c::;:kXKK0OxooollldxONWMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMNKOkdocccclccccccodxxkx;.',;:clollc:;;cc::cxdoxOXWMMMMMMMMMMMMMMMMMMMMMM
MMMMMMWKOkkxddxkOxl;:locl:''.';:coolc;'..,:c:;::;;codxkxd0WMMMMMMMMMMMMMMMMMMMMM
MMMMMN0kkkxdooolc;';ccc:clldl,'''........,ldoc::;,coccx0Ox0WMMMMMMMMMMMMMMMMMMMM
MWXXKOkkxxkOOOd;',ldxxxxdodOd;ld;'..:dl;,:dxdl::c,'::,:x0OkKWMMMMWNK00KXWMMMMMMM
MWkokkxxkO000d;'cxOOkdoll:cdccOXk:.,xXOl;:clloldd:.':::ldxoxNMWKkxoclloodx0NMMMM
MXo:odddddxxo;';xKOo::lddoolcokOo,..;dko:ccodkdc;...':lc;,,:lxkxxkOOKXKOkdlo0WMM
WOl::lodlllc,.':codl::ccoOOook0x:''..:OkooldxkKd'.....,:::;,.:OKKKKNNNXK0OkdlkWM
WOcllcldddoc'.;c:okxo:;:x0xcoK0c''''..ckOdllodoxc........'...cO0KKKKKXXXK0OOdlOM
M0lclloxxdl;..,:;clxxooOOxoloOx:'''''';dxdlcloccdc...........,oddxOKKXXKKK0OkldN
MNklcclodlc,..',,,lxdlxOkdllokK0o,'',okxxdl:llc;x0c...........',..,xKKKKKKOkkdoK
MMW0ocllool;...,',ldl,:loolllo0XKd,,oO0xoolccc:;xWKc...............l0KKK00OkkdoK
MMMMXxlclooc'...'.',;;cocccllxO0OOddkkkxdoc::::lKMMXl.............:kKKKOkkxxxoxN
MMMMMWKxlc:c;.......';:oddddxxxxxddddollccccldONMMMMNx'..........o0KK0xolllllxXM
MMMMMMMWXOdc:,. ......',;cll:cccccc:;,;lddoldXMMMMMMMWKo'........:OOxocc:::cxXMM
MMMMMMMMMMWXOo,. .......;;:;''.....';lkXX0xdodKMMMMMMMMWXkl,......:c:;:lodx0WMMM
MMMMMMMMMMMMMN0xoc,....,dOko:,',:lx0XWMMWXOkdo0MMMMMMMMMMMWNK000000OO0KXNWWMMMMM
MMMMMMMMMMMMMMMMMWNK0Okkkkxld0KXNWMMMMMMMNOxdokXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMN0xolxNMMMMMMMMMMMN0OOkxxk0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMWNK0kdxk0NMMMMMMMMMMMWNXKKK00KNMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMN0OOO0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
"""
        personaje["hp"] = random.randint(50,80)
        personaje["atq"] = random.randint(5,10)
        personaje["def"] = random.randint(5,10)
        personaje["vel"] = random.randint(40,50)
        personaje["esperanzaVida"] = random.randint(50,80)
        zonaNacimiento = ["Green Bit"]
        personaje["nacimiento"] = islaNacimiento()
    elif raza == "lunarian":
        personaje["arte"] = r"""
MMMMMMMMMMMMMMMWKdlo0WMMMMMMMMMMMMMMMMMMMWWMMMMMMMMMMMMMMMMMMK;  .c0WMMMMMMMMMMM
MMMMMMMMMMMMMWKl.   lWMMMMMMMMMMMMMMMWWNX0KWMMMMMMMMMMMMMMMMMO.    .oXMMMMMMMMMM
MMMMMMMMMMMMNx'    .OMMMMMMMMMMMMMMMN000O00KWMMMMMMMMMMMMMMMM0'      ;0WMMMMMMMM
MMMMMMMMMMMKc.     ,KMMMMMMMMMMMMMMWKOkO00OOOKWMMMMMMMMMMMMMMX:       .kWMMMMMMM
MMMMMMMMMWO,       ,KMMMMMMMMMMMWXK0OOddKXX0O0KNMMMMMMMMMMMMM0,        .kWMMMMMM
MMMMMMMMWk'        ;XMMMMMMMMMMWX0kxdo,':lookOOKXNWMMMMMMMMMWo          .kWMMMMM
MMMMMMMWx.         .kWMMMMMMMWNK0ko;';'..,,;oxO0O0NMMMMMMMMWk.      .    .kWMMMM
MMMMMMWx.    .      ;KMMMMMMWKOOOko;:oc;:cc,cxkxxxKWMWWMMMWx.      ...    ,0MMMM
MMMMMWk.    ....... .cXMMMWWN0dlccc,';,..',.,:cldOKNNNWMMXl.    ..... .    cNMMM
MMMMM0,    .. .....  .:KWXKKNKkollc'........'d00O00XXXWNx,   .. ..  ....   .xWMM
MMMMX:    .   . .....  ,xO0NWMNK0O:..........'dkkkOXWXx,   ...         .    '0MM
MMMWo.           .....  .,oKWWX0x; .,..... .'..coxkxl,    ...  ..       .    lNM
MMMO'            .......   .:oolc..,.  ...  .,,lc..         ......      ..   '0M
MMX:         . .. .....    .   .cdc.   .'.   'dd,... ...   ... .. .      .   .dW
MWx.         . ...       .....'''clc;. .,.. ,c:.'cdd:..  ....          .      :X
MX:    ...   ...   .   .....:dxo,..cddo:;cool;. .;::;.    ......       .. .   .O
Mk.           ...  .....   .,::,.....:odkkx:.  .. ....    .....  .  ......     o
N:             .........   ....  ..   .,;;.    ..        .....   .             ,
O.      .      .    .. ..            .                   ....                  .
o      .';;.   .    .. ..            ... .'...      .......       .            .
;      .cxd;.  .   . ....        ... .'. .'...   ....,'.    .  ....        .    
'      .':c:. ..   ......       ...    . ...    .',..;;.         ..             
.       ..;c:'.. .................'.............',...;;.         .              
          .;c:,......     ';'.,;...          ...';...;:,...;;'....              
           .,cc;'...     .,;..';..     ..  ..   .;. .,:.   ......               
            .,:c;,',:,....;;..,;'........      .... .,,.    ..          .       
             .':c::lc'.  .';..',',,.          ;xl.  ....                .. .    
.             ..:c:;'.',,'..  . .ol.          ...     ..                       .
'               .,:c::lddd;      ...            .    ...                       ;
:               .'::::cdkx:.     ,c'           :x:   . ..                      o
x.               'ccc:cdko.     .cx:           .'.   .  ..                    .O
K;               .,cl::lc.       ..                  .  ..                    :X
Wx.               ..'....        ..            .;,.  ..  ..  .               .dW
MXc    .          .... .        .lkc.          .oo.  ..  ..                  '0M
MM0'             .''. ..         .'.                 ..   .                  oWM
MMWk.            .''. ..    .                         ..  .                 '0MM
MMMWd.         .........  .'.  ..'.            .,'....  .''...              oWMM
MMMMNl       .';,''.......;:.   .,,...  .   ...;;.  .,'''.....             ,0MMM
MMMMMXc      .';;;,,'.....cc.    .',;;'...  .','   .';,...,,'.             oWMMM
MMMMMMXc      .';;,;,,,,...',,.   .,coc,''. ...   .;;,,,,,'..             ;KMMMM
MMMMMMMX:      ..,;,...,;;;..';'   .,;;;;;'. ..  ':,..::'.    .          .xWMMMM
MMMMMMMMXl.      ....   .:l;. .',.....'',;c:'...':'.':;'.                lNMMMMM
MMMMMMMMMNo.            .'',:,. .'.   ...':oo:'.,'..;,...               :XMMMMMM
MMMMMMMMMMNx.           ..  .,;....    ....,coo:'..,'. ..              ,0MMMMMMM
MMMMMMMMMMMWk.      .   ..    .,'     ..    .,col;;,.  ..             ,0MMMMMMMM
MMMMMMMMMMMMWx.         ..     ...    .cxxl,. .,cl;.    ..           'OMMMMMMMMM
MMMMMMMMMMMMMNo.        ..            .kWWWXl.  .',.    .'..        'OWMMMMMMMMM
MMMMMMMMMMMMMMX:     .':lc;'.        .lXMMMM0;    ..   'coddl;.    'OWMMMMMMMMMM
MMMMMMMMMMMMMMMk.  .'col:;coc.      .,0MMMMMKl'.      ;xdc,;lo:.  .kWMMMMMMMMMMM
MMMMMMMMMMMMMMMNc  .cdl.  ;ol. .  ..'kWMMMMMWW0:.    .lxd;..co;;,'oNMMMMMMMMMMMM
MMMMMMMMMMMMMMMMk. .;ool:col,  .  ;oxXMMMMMMMMW0d'    ,loddol,..;:cxXWMMMMMMMMMM
MMMMMMMMMMMMMMMMK,   .;c:;,.    .'oXMMMMMMMMMMMMXc..   ..',..   .,;lxOKNMMMMMMMM
MMMMMMMMMMMMMMMMX;    ..      ..,kXWMMMMMMMMMMMMW0:       .    .cxdooddk0KNWMMMM
MMMMMMMMMMMMMMMM0,    ..     ...lXMMMMMMMMMMMMMMMWKd,.    .... .oXWKkdoolld0WMMM
MMMMMMMMMMMMMMMWk'.  .'.    ..:xXMMMMMMMMMMMMMMMMMMWO:.    .,.  'OMMMNKkooxKWMMM
MMMMMMMMMMMMMMMK:.   ...   .':0MMMMMMMMMMMMMMMMMMMMMM0;.  ..'.  .kWMMMMWNXNMMMMM
MMMMMMMMMMMMMMNl. ...''..  c0NWMMMMMMMMMMMMMMMMMMMMMMWk.    ... .cXMMMMMMMMMMMMM
MMMMMMMMMMMMMNo.''...... ..:KMMMMMMMMMMMMMMMMMMMMMMMMM0;. ....  .,kWMMMMMMMMMMMM
MMMMMMMMMMMMMN00XKc  ..   ;ONMMMMMMMMMMMMMMMMMMMMMMMMMN0l. ..   'xXWMMMMMMMMMMMM
"""
        personaje["hp"] = random.randint(180,250)
        personaje["atq"] = random.randint(40,60)
        personaje["def"] = random.randint(30,50)
        personaje["vel"] = random.randint(20,30)
        personaje["esperanzaVida"] = random.randint(150,250)
        zonaNacimiento = ["desconocido"]
        personaje["nacimiento"] = islaNacimiento()
    elif raza == "bucanero":
        personaje["arte"] = r"""
MMMMMMMMMMMMMMMMMMMMMMMMMMWNNWWNXNNXkoodxONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMXdllkKKKKKkc:lc;c0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMWk:cx0KK0KK0klclokNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMXdldxxolodl:;:dOKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMXl,;ddc;coc.....;0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMXl.:kkdoooc'.....:x0O0XNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMM0:.:kOkdolc,..........,:kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMWKxkkxxk00x:;;,'............;xXWMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMM0:'dO0XXKKo'......'''.........;lkNMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMWO;,k00XXXKo'..........'''.... ...:OWMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMKc.,kKKXKko:......'''',,,,;;;,'....,dXMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMXl':dKNNXO;.......''',,;;::ccccll:;,,,oXMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMO;c0XXWN0d,........''',,;::::ccclllllllxO0XWMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMNxldKNNN0c.........''',,;;:::cccccclllllllloxO0XWMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMXxldKXKNWXk;........'''',,;;::::c:::::ccccllllooooxOKNWMMMMMMMMM
MMMMMMMMMMMMMMWKl,;xXNNN0l;'......''',,;;;:::::c:::;;;;:::::ccclllllcldOKWMMMMMM
MMMMMMMMMMMMW0o;;xKXNWMWk;...'''',,,;;;;;:::::::::;;;;;;,,,,;;;;:;;,,''',ckNMMMM
MMMMMMMMMMMNx;..:0WNNWWXd;'''''',,,,;;;;;;:::::::;;,,,,,'''''''''.........'lKMMM
MMMMMMMMMWKl,.';dXXKXNWNX0Okxoc;,',,,;;;;;;;;;;;;;,,'''''...................lXMM
MMMMMMMWKd;';lkKNNKXWWWWWWWWWNX0xl;'',,,,,,,,,,,,,''''......................,kWM
MMMMMWKd;';d0NNWNXXWWWWWWWWWWWWWNXOo;'''',,,,,,,,''..........................oNM
MMMMNx:',o0NNNWWXXNWX00KNWWWWWWWWNNXOl,..'''''''''...........................cXM
MMW0c'':kXNK0XWNXNWWk:;cox0XWWWWWWNNXKx:'....'...............................:KM
MWk,.,o0NKx:lO0OkOOkdlccc:cokXWWWNNNXXXOxl'..................................;OM
MXl.'oKXk:,';::clllooollcc:::ckXNNNNXXXXX0o'.................................'xW
MXl'lKXx;',,,,,:c:cc:;,'''''..'cOXXXXKKKKK0o'.................................lN
MWxcOXx,.''''',;::ccc:,'........,d000000000Oo'..............  ............''..cX
MMKkKKl....'',;:cccccc;,'........'dKK0000000kc..............   ...............;0
MMN00Kd,...'',,;c:::::;;,''....,clkKKKKKKKKKKd;.............    ..............:0
MMWOxO0l..'''''',,'''''''''....lKXXXXXXXXXXXXKOkxxdolc:,'..     ..............cX
MMMOclOOc..'....,;,,'''........c0XXXXXXXXXXXXXXXXKKK00Okdl:,..  ...''.........cX
MMM0;,xKo'.....';clllc;,'......c0XXXXXXXKXXXXXXXKKK00OOkxdddoc,...';,'........:K
MMMKc,oKk;....',;ccccc:;,'.....:OXXXXXXXXXXXXXKKK00OOkkxxdxxdl:'..',;,'.......,O
MMMWO;:OKx,.'''';:;;;;;;,'.....,xO0KXXXXXXXXKK000Okkkkxxxxxxdl:;c;',,,,'......'x
MMMM0:;dK0c''''',;,,,,,,,,'.....'';xKXXXXXXK0dcccllodxxxddxdoccxXk,',,,'......'x
MMMMO;,:dx:'''''',,'',,,,,'......'l0XXXXXXXKx,........',;:ccclkNMXl'',,'.....',d
MMMMk;,,:dl''''..','''',,''.....,d0XXXXXXXKk:.........   ...,dNMMM0;..''......'d
MMMMk,,',od,...'',;;;;;,'''...'lkKXXXXXKKKk:................lXMMMMNo..,,,'.....o
MMMNd''..cOl'.'o00OOKXO:'''';lkKXXXXXKKK0x;...............'dNMMMMMWO,.,;;,,''''o
MMMXl....'x0d:,dNWXXWWXo,:ok0XXXXXXKKKOo:,...............:OWMMMMMMMK:',:::;''''d
MMMK:.'...c0XKO0NWNXNWWK0XWNNXXXXKKK0d;................'oXMMMMMMMMMO;';:c:;'..'x
MMNd;,,'..'dXNNNWWNXNWWWWWWWNXXKKKOo;.................:OWMMMMMMMMMWk,';:c:,...;O
MM0c:cc;...,xXNNWWWXXWWWWWWNNXK0xl,..................oXMMMMMMMMMMMMO;';::,....:0
MMO::c:,...,:dKNNWWXXWWWWWNKOdl;',lc'...............oNMMMMMMMMMMMMMXl';:;'....lX
MMO:::;.. .:;;co0NWXXWWW0xl:,;l:',lo:'';c;...'..'..;0MMMMMMMMMMMMMMWk,,;,....'dW
MM0c;;'...,xxc,'xNWXXWWXo;;,,:lodkOOkdl,'....,;cc;;xWMMMMMMMMMMMMMMM0:,;,'...,OM
MMKc;,....lKO;.;kXXKKNNk;.....;x00Okkkxoc;....:lc:oXMMMWWMMN0O0KXNNWXl,:,'...cKM
MM0c;,...;OKOc.'dXNKKNNKo,,,,,cOK00OOOkxxc....;c::oXMMNXNMMKdllllollc,,:,'...oNM
MWk:;'...oX0o'.'xNWXXWWNx:;,,':k000OOOkxo;....':c:oXMMNKNMMXxllccc:,..';,'...dWM
MNd;,.. 'kXk;..'dNWXXWWNk;,,,,;:dkOOOxo;'......';;cKMMNKXMMNkoolccl:..';;,'.'dNM
MNkc;...oKOc,'',dNWNXWWWOlccc::;,,,,,'..........';l0MMWKXMMNklccccl:..,::;,,oKWM
MNxc;'.'xWWKkxddkO0OOO00xolllcccccccllooollc::;;oKWWMMWKXMMWOlcccc:;,;cc:;,:OWMM
WOlll;..:KMWXK00000KK00000OkkkkkkxkO00OOkkdollc:dNMMMMWXXMMW0occc:::cllc::;c0MMM
Koccdl,.:0MMWX0OOkkOOkkOOOkxdooooxO0000OOkxdollcdXMMMMWXXWMW0olcc::cc:;::;;:kWMM
klcclc,.'lXMWWX0OkkkxkkxxxxdoolclkO0KK00OkxdollcdXMMMMMXKWMMKdlc:;:lc;,;;;;;dNMM
KOko:'.';xNMWWNK00OOkxxdddoolloook0KKKK0OOkxoolcdXMMMMMXKWMMXdc:;,:l:'';;;;;lXMM
MMWX0kkOKWMMMMWXK0OOkxxdoolloONXOk0KXKK0OOkdoolldKMMMMMNKXNXOocc;,;;,..,,,,,lKMM
MMMMMMMMMMMMMWNXK0Okxdoooood0WMMWX00KKKOkxolooolo0MMMMMMWNNX0xl;'..''.'''',ckNMM
MMMMMMMMMMMMMMNX0Okxdxxxxoo0WMMMMWNKKKKKKOxddooolOWMMMMMMMMMMWKxl:;;;;::ldONMMMM
MMMMMMMMMMMMMMWX0OxdxxxdolkNMMMMMMMNK0KKKK0OkxdolkNMMMMMMMMMMMMMWNXKXXXNWMMMMMMM
"""
        personaje["hp"] = random.randint(150,200)
        personaje["atq"] = random.randint(25,35)
        personaje["def"] = random.randint(25,35)
        personaje["vel"] = random.randint(15,25)
        personaje["esperanzaVida"] = random.randint(100,200)
        zonaNacimiento = ["desconocido"]
        personaje["nacimiento"] = islaNacimiento()
    elif raza == "tres ojos":
        personaje["arte"] = r"""
MMMMMMMMMMMMMMMMMMMWNNXXNWMWNKOkdoolloooodxOKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMWXkl:;,,;lddl:::::ccclcccc:;;coooxKWMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMWKxc,......,:cccllcclooollllc:::;,..:0WMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMKl;,.. ..;loolcc::ccc::,';::cldxxddc'cXMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMNo;,.  ..:xOkdoc:ldxxxdc,',,;lxO00KX0olKMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMM0c,.. ..cxkkxdl:lxkk00d;,;'...cOKKKKKOx0WMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMNx:;....;dkkdoc;;ldxOOo;,:c:,,'';dOOOOkdxXMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMWKc;ll,..;oxxdol;,;:clc;',:lc;,'...,;:cloodKMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMWk,.c0Oc',oxxdddc,,;'''...,c:;'....,;;'',:cdXMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMWk,.'dXXd,;dkkoll;';'.....':odddooodxdo:'.';oKMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMWO;..'dXXOc;oxdolc,';'..;;;:ldxkOOOOOOxo:'..,dNMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMXl'..'c0XKx:;llc:,.','.,,....':dOOO0Oo,'....,xWMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMKc',,',oKX0o,,:l;..';'.':;',;oxkOkkkoc:::;,.,xWMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMXl;:c:,;d0KOl''cc'.','':oddxkOOO0OOOd:::'...lXMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMNx:ldxo;;cdxo;..',;;,';codxkOOkkOOOOdc:,. ..dWMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMKoo0X0xc,',;;'......';lkkxkOOkxxxxdddl,....cKWMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMWOlOXXKxc,..,,........,lxk00xl::::ldo,....,:xNMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMWk;ckKKOoc;'.''.....'..':dOKKkoccllc'...,cdkKNMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMW0o,..;okOxoc;'''..:ooc;,,,,,:clllll;....':d0XNMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMNx,...',;:loolc,'''l00oloc;;;,....,:oxo:',;ldxkXMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMWd'..'',:cclc::c;''c0N0llxdlcc:;,'.;ldKXkloddl:l0WMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMKc,;;::;cooolc;;'.,xNWOllxkxdolc:;,,;lOXXOxxoclkKNMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMXl,cdxxxdcclolc,. .:kKN0ocxOOkxdoll:,':x0kc,'';cxXWMMMMMMMMMMMMMMMMMMMMMMMMMM
MNO:.;xKXKOko:;:::;.....,oxdccxOOOkkxdo;';ol.  .;cllOWMMMMMMMMMMMMMMMMMMMMMMMMMM
Nx;,,:d0XKkoccloolc:,.   .:ll::ldxkkkxl:;;:,.  .codx0NMMMMMMMMMMMMMMMMMMMMMMMMMM
Ko:coooxOOo:cdxxooollc,   'clolloodxxdoddl;;,. .:dkXWMMMMMMMMMMMMMMMMMMMMMMMMMMM
KocoOKKOxoccodooodxkkxd;. .;ldxooxxxxxxxxxlclc..'o0WWMMMMMMMMMMMMMMMMMMMMMMMMMMM
WKdoxKXX0l;cooloxO0KXK0k;. .:dxkdodxxxxxxxxoldc..cKWMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMWkclxxxl;:loddxKX00K00x;. .lxkkdloxxddxkkxlod;.cKWMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMNklol;,;clodkO0X0OOOOOx,. 'oOOOxoodxxdk00xdko',kXWMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMWKkd;.,codx0KK0kkkkO00d,..,d000OxxOKKKXNXkO0:'l0NWMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMWKl,;ldxO00K0xxxOKXXKd'..:kKXXXK0KNNXNNO0Xd.:OKNMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMNKX0c,codkOKKK0kxOKNWWWXd'.,dXWWWWN0OKKKKk0Nx,;ONWMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMM0c::,;coxk0KXNKxdOXWMMWWKdllo0WMMMWKOkkxdkXWk:c0WWMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMW0d;,:oxk0KXXXNOdOXWMMMMWXkdokNMMMMNXkollOWWkcdXWWMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMW0c:ldk0KXNNXXXxdKWMMMMMWk:;c0WMMMWNOlcxNWNkoONWMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMW0c;cok0KNWWMWNXkloOXNWWNNk,..oKKKKKKkoxXWWKxkXWWMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMW0l;;cxO0XWWMMMWKxc;cdOKKKKk,  ,oddxxxxkKNWXOxONWMMMMMMMMMMMMMMMMMMMMMMMMMMMM
"""
        personaje["hp"] = random.randint(90,130)
        personaje["atq"] = random.randint(12,22)
        personaje["def"] = random.randint(12,22)
        personaje["vel"] = random.randint(10,20)
        personaje["esperanzaVida"] = random.randint(100,150)
        zonaNacimiento = ["Totto Land"]
        personaje["nacimiento"] = islaNacimiento()

def islaNacimiento():
    zonaNacimiento = ["East Blue", "West Blue", "North Blue", "South Blue", "Grand Line", "Red Line"]
    zona = random.choices(zonaNacimiento,weights = [20,20,15,15,25,5], k =1)[0]
    if zona == "East Blue":
        isla = random.choice(["Isla Dawn", "Shells Town", "Isla Orange", "Isla Conomi", "Baratie", "Isla Gecko", "Loguetown"])
        personaje["hp"] += personaje["hp"]*0.05    
    elif zona == "West Blue":
        isla = random.choice(["Ohara", "Isla Pucci", "Isla Ilusia", "Isla de la Mafia"])
        personaje["def"] += personaje["def"]*0.05
    elif zona == "North Blue":
        isla = random.choice(["Flevance", "Spider Miles", "Isla Swallow", "Lvneel", "Fiora"])
        personaje["atq"] += personaje["atq"]*0.05
    elif zona == "South Blue":
        isla = random.choice(["Baterilla", "Isla de la Armada Revolucionaria"])
        personaje["vel"] += personaje["vel"]*0.05
    elif zona == "Grand Line":
        isla = random.choice(["Whisky Peak", "Little Garden", "Isla Drum", "Alabasta", "Jaya", "Skypiea", "Sabaody", "Isla Gyojin", "Dressrosa", "Zou", "Wano", "Whole Cake Island", "Elbaf", "Laugh Tale"])     
        personaje["hp"] -= personaje["hp"]*0.05    
        personaje["def"] += personaje["def"]*0.05
        personaje["atq"] += personaje["atq"]*0.05
        personaje["vel"] += personaje["vel"]*0.05    
    elif zona == "Red Line":
        personaje["def"] += personaje["def"]*0.1
        personaje["vel"] -= personaje["vel"]*0.05  
        isla = random.choice(["Mary Geoise", "Red Port"])
    return isla


def menu():
    print(r"""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⠀⠀⠀⢠⣾⣧⣤⡖⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠋⠀⠉⠀⢄⣸⣿⣿⣿⣿⣿⣥⡤⢶⣿⣦⣀⡀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡆⠀⠀⠀⣙⣛⣿⣿⣿⣿⡏⠀⠀⣀⣿⣿⣿⡟
    ⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠷⣦⣤⣤⣬⣽⣿⣿⣿⣿⣿⣿⣿⣟⠛⠿⠋⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠋⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⡆⠀⠀
    ⠀⠀⠀⠀⣠⣶⣶⣶⣿⣦⡀⠘⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠈⢹⡏⠁⠀⠀
    ⠀⠀⠀⢀⣿⡏⠉⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡆⠀⢀⣿⡇⠀⠀⠀
    ⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡘⣿⣿⣃⠀⠀⠀
    ⣴⣷⣀⣸⣿⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⠹⣿⣯⣤⣾⠏⠉⠉⠉⠙⠢⠀
    ⠈⠙⢿⣿⡟⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣄⠛⠉⢩⣷⣴⡆⠀⠀⠀⠀⠀
    ⠀⠀⠀⠋⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣀⡠⠋⠈⢿⣇⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ONE PIECE GAME
    """
    )
    print("1. Crear partida")
    print("2. Cargar partida")
    print("3. Salir")
    opcion = int(input("Introduce una opción: "))
    return opcion

op = menu()

