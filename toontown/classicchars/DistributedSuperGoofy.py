from pandac.PandaModules import *
from . import DistributedCCharBase
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM, State
from direct.fsm import State
from toontown.classicchars import DistributedDowntownToontown
from . import CharStateDatas
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from . import DistributedCCharBase


class DistributedSuperGoofy(DistributedDowntownToontown.DistributedDowntownToontown):
    notify = DirectNotifyGlobal.directNotify.newCategory(
        'DistributedSuperGoofy')

    def __init__(self, cr):
        try:
            self.DistributedDowntownToontown_initialized
        except BaseException:
            self.DistributedDowntownToontown_initialized = 1
            DistributedCCharBase.DistributedCCharBase.__init__(
                self, cr, TTLocalizer.SuperGoofy, 'sg')
            self.fsm = ClassicFSM.ClassicFSM(
                self.getName(), [
                    State.State(
                        'Off', self.enterOff, self.exitOff, ['Neutral']), State.State(
                        'Neutral', self.enterNeutral, self.exitNeutral, ['Walk']), State.State(
                        'Walk', self.enterWalk, self.exitWalk, ['Neutral'])], 'Off', 'Off')
            self.fsm.enterInitialState()
            self.nametag.setName(TTLocalizer.Goofy)

    def walkSpeed(self):
        return ToontownGlobals.SuperGoofySpeed
