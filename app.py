from flask import Blueprint, redirect, url_for
from flask_restful import Api
from resources.Auth import Signup, Login
from resources.Landing import Landing
from resources.Profile import ProfileFetch, InputProfile, ProfileFetchUser
from resources.Dokter import DokterFetch, InputDokter, DokterFetchPersonal
from resources.Jadwal import JadwalFetch, InputJadwal
from resources.Antrian import AntrianFetchAll, AntrianFetchDate, AntrianFetchJadwal, AntrianFetchLast, AntrianFetchProfile, AddAntrian, UpdateAntrian, AntrianFetchProfileAll,AntrianFetchAllAt
from resources.Search import Search, SearchNone

api_bp = Blueprint('api', __name__)
api = Api(api_bp)


# Route
api.add_resource(Landing, '/')
api.add_resource(Signup, '/signup')
api.add_resource(Login, '/login')
api.add_resource(ProfileFetch, '/profile') #show profile for debug
api.add_resource(InputProfile, '/profile/add') #add profile for debug
api.add_resource(ProfileFetchUser, '/profile/user')

api.add_resource(DokterFetch, '/dokter') #show profile for debug
api.add_resource(InputDokter, '/dokter/add') #add profile for debug
# api.add_resource(DokterFetchPersonal, '/dokter/fetch') #replaced by search function

api.add_resource(JadwalFetch, '/jadwal')
api.add_resource(InputJadwal, '/jadwal/add') 


api.add_resource(AntrianFetchAll, '/antrian/all')
api.add_resource(AntrianFetchAllAt, '/antrian/at/<jadwalId>/<tanggal>')

api.add_resource(AntrianFetchDate, '/antrian/tanggal/<tanggal>') 
api.add_resource(AntrianFetchJadwal, '/antrian/jadwal/<jadwalId>')
api.add_resource(AntrianFetchLast, '/antrian/terakhir/<tanggal>')
api.add_resource(AntrianFetchProfile, '/antrian/pasien/<tanggal>')
api.add_resource(AntrianFetchProfileAll, '/antrian/pasien')


api.add_resource(AddAntrian, '/antrian/add') 
api.add_resource(UpdateAntrian, '/antrian/update') 

api.add_resource(Search, '/search/<data>')
api.add_resource(SearchNone, '/search/') 






api_index = Blueprint('index', __name__)
@api_index.route('/', methods=['GET'])
def index():
	return redirect(url_for('api.landing'))
