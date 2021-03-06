#imports
import math
import jupyter
import time

#functions

def wait(amount):
    time.sleep(amount)
    print()

#Welcome message

print('Welcome to Pinecone Sound inventory check')
wait(1)
print('Select category: kit, microphones, recorders, mixers, headphones, monitors, amplifyers, accessories, studio.')

#This is a dictionary of all kit held by Pinecone Sound, its quantity, and location.

kit_list={
'rode ntg2':'01 in location kit',
'seelectronics 4400a':'01 in location kit',
'sony ecm77b':'02 in location kit',
'lom elektrousi':'01 in location kit',
'luhd pm01ab':'01 in location kit',
'tram tr50':'01 in location kit',
'talkstar ta58':'02 in storage',
'red5 audio rv6':'01 in storage',
'audio technica atm350cw':'01 in location kit',
'jrf hydrophone':'02 in location kit',
'tascam dr40':'01 in location kit',
'tascam dr05':'01 in loation kit',
'zoom f4':'01 in location kit',
'sqn 4s mini':'01 in office',
'sony mdr7506':'01 in office, 01 in location kit',
'peavey pro15':'02 in office',
'dare audio v500':'01 in office',
'rode blimp':'01 in location kit',
'rycote mini windjammer':'02 in location kit',
'rycote 65501':'01 in location kit',
'audio technica at8533':'03 in location kit',
'rode vxlr':'02 in location kit',
'mini boom mic stand':'01 in location kit',
'rode boompole': '01 in location kit',
'cp cases ems':'01 in office',
'apple imac':'01 in office',
'maudio fast track pro':'01 in office',
}

microphones={
'rode ntg2':'01 in location kit',
'seelectronics 4400a':'01 in location kit',
'sony ecm77b':'02 in location kit',
'lom elektrousi':'01 in location kit',
'luhd pm01ab':'01 in location kit',
'tram tr50':'01 in location kit',
'talkstar ta58':'02 in storage',
'red5 audio rv6':'01 in storage',
'audio technica atm350cw':'01 in location kit',
'jrf hydrophone':'02 in location kit',
}

recorders={
'tascam dr40':'01 in location kit',
'tascam dr05':'01 in loation kit',
'zoom f4':'01 in location kit',
}

mixers={
'sqn 4s mini':'01 in office',
}

headphones_monitors={
'sony mdr7506':'01 in office, 01 in location kit',
'peavey pro15':'02 in office',
}

amplifyers={
'dare audio v500':'01 in office',
}

microphone_accessories={
'rode blimp':'01 in location kit',
'rycote mini windjammer':'02 in location kit',
'rycote 65501':'01 in location kit',
'audio technica at8533':'03 in location kit',
'rode vxlr':'02 in location kit',
'mini boom mic stand':'01 in location kit',
'rode boompole': '01 in location kit',
}

studio_accessories={
'cp cases ems':'01 in office',
'apple imac':'01 in office',
'maudio fast track pro':'01 in office',
}

#A list of user friendly names

kit=kit_list.keys()
kitlist=kit_list.keys()
microphone=microphones.keys()
microphones=microphones.keys()
recorder=recorders.keys()
recorders=recorders.keys()
mixer=mixers.keys()
mixers=mixers.keys()
headphones=headphones_monitors.keys()
monitors=headphones_monitors.keys()
amplifyer=amplifyers.keys()
amplifyers=amplifyers.keys()
studio=studio_accessories.keys()
accessories=microphone_accessories.keys()


#Trying to make item search more user friendly

rodentg2=kit_list['rode ntg2']
rode_ntg2=kit_list['rode ntg2']
seelectronics4400a=kit_list['seelectronics 4400a']
seelectronics_4400a=kit_list['seelectronics 4400a']
sonyecm77b=kit_list['sony ecm77b']
sony_ecm77b=kit_list['sony ecm77b']
lomelektrousi=kit_list['lom elektrousi']
lom_elektrousi=kit_list['lom elektrousi']
luhdpm01ab=kit_list['luhd pm01ab']
luhd_pm01ab=kit_list['luhd pm01ab']
tramtr50=kit_list['tram tr50']
tram_tr50=kit_list['tram tr50']
talkstarta58=kit_list['talkstar ta58']
talkstar_ta58=kit_list['talkstar ta58']
red5audiorv6=kit_list['red5 audio rv6']
red5_audio_rv6=kit_list['red5 audio rv6']
audiotechnicaatm350cw=kit_list['audio technica atm350cw']
audio_technica_atm350cw=kit_list['audio technica atm350cw']
audiotechnica_atm350cw=kit_list['audio technica atm350cw']
jrfhydrophone=kit_list['jrf hydrophone']
jrf_hydrophone=kit_list['jrf hydrophone']
tascamdr40=kit_list['tascam dr40']
tascam_dr40=kit_list['tascam dr40']
tascamdr05=kit_list['tascam dr05']
tascam_dr05=kit_list['tascam dr05']
zoomf4=kit_list['zoom f4']
zoom_f4=kit_list['zoom f4']
sqn4smini=kit_list['sqn 4s mini']
sqn_4smini=kit_list['sqn 4s mini']
sonymdr7506=kit_list['sony mdr7506']
sony_mdr7506=kit_list['sony mdr7506']
peaveypro15=kit_list['peavey pro15']
peavey_pro15=kit_list['peavey pro15']
dareaudiov500=kit_list['dare audio v500']
dare_audio_v500=kit_list['dare audio v500']
rodeblimp=kit_list['rode blimp']
rode_blimp=kit_list['rode blimp']
rycoteminiwindjammer=kit_list['rycote mini windjammer']
rycote_mini_windjammer=kit_list['rycote mini windjammer']
rycote65501=kit_list['rycote 65501']
rycote_65501=kit_list['rycote 65501']
audiotechnicaat8533=kit_list['audio technica at8533']
audio_technica_at8533=kit_list['audio technica at8533']
rodevxlr=kit_list['rode vxlr']
rode_vxlr=kit_list['rode vxlr']
miniboommicstand=kit_list['mini boom mic stand']
mini_boom_mic_stand=kit_list['mini boom mic stand']
rodeboompole=kit_list['rode boompole']
rode_boom_pole=kit_list['rode boompole']
cpcasesems=kit_list['cp cases ems']
cp_cases_ems=kit_list['cp cases ems']
appleimac=kit_list['apple imac']
apple_imac=kit_list['apple imac']
maudiofasttrackpro=kit_list['maudio fast track pro']
maudio_fast_track_pro=kit_list['maudio fast track pro']
