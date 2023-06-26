import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

from cobinder.shared.utils import clear_mem
from cobinder.af.model import mk_af_model

# backward compatability
mk_design_model = mk_afdesign_model = mk_af_model