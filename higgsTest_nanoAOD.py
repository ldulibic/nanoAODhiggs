import ROOT
from math import hypot
import sys

ROOT.gROOT.SetBatch()
ROOT.gStyle.SetOptStat("nemruoi")
ROOT.gROOT.ForceStyle()

from optparse import OptionParser
parser = OptionParser()

parser.add_option('--maxEvents', type='int', action='store',
                  default=-1,
                  dest='maxEvents',
                  help='Number of events to run. -1 is all events')

parser.add_option('--reportEvery', type='int', action='store',
                  default=100,
                  dest='reportEvery',
                  help='Report every N events')

parser.add_option('--mX', type='int', action='store',
                  default=3000,
                  dest='mX',
                  help='X scalar mass')

parser.add_option('--mY', type='int', action='store',
                  default=300,
                  dest='mY',
                  help='Y scalar mass')

parser.add_option('--massPoint', action='store',
                  dest='massPoint',
                  help='Mass point')

parser.add_option("--withNu", action="store_true",
                  dest="withNu",
                  help="Include neutrinos in GenJets",
                  default=False)

(options, args) = parser.parse_args()

def DeltaPhi(v1, v2, c = 3.141592653589793):
    r = (v2 - v1) % (2.0 * c)
    if r < -c:
        r += 2.0 * c
    elif r > c:
        r -= 2.0 * c
    return abs(r)

# single input file for testing
ifile = "./data/TRSM_XToHY_6b_M3_2800_M2_700_NANOAOD.root"

# open root input file directly 
evtFile = ROOT.TFile.Open(ifile)
events  = evtFile.Get("Events")

# loop over events 
for i, event in enumerate(events):
    genParticles = event.GenPart_pdgId
    nParticles   = event.nGenPart
    #jets         = event.GenJet
	
    print(genparticles[i])
    print(i)
    break

