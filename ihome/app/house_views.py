

from flask import Blueprint, redirect, render_template, jsonify, session, request
from app.models import User, House, Area, Facility
from utils import status_code
from utils.functions import is_login

house_blueprint = Blueprint('house', __name__)


@house_blueprint.route('/myhouse/', methods=['GET'])
@is_login
def myhouse():

    return render_template('myhouse.html')


@house_blueprint.route('/authmyhouse/', methods=['GET'])
@is_login
def auth_myhouse():
    user = User.query.get(session['user_id'])
    if user.id_card:
        houses = House.query.filter(House.user_id == user.id).order_by(House.id.desc())
        hlist_list = []
        for house in houses:
            hlist_list.append(house.to_dict())

        return jsonify(hlist_list=hlist_list, code=status_code.OK)

    else:
        return jsonify(status_code.MYHOUSE_USER_IS_NOT_AUTH)


@house_blueprint.route('/newhouse/', methods=['GET'])
@is_login
def newhouse():
    return render_template('newhouse.html')


@house_blueprint.route('/areafacility', methods=['GET'])
@is_login
def area_facility():
    areas = Area.query.all()
    area_list = [area.to_dict() for area in areas]

    facilitys = Facility.query.all()
    facility_list = [facility.to_dict() for facility in facilitys]

    return jsonify(area_list=area_list, facility_list=facility_list)


@house_blueprint.route('/uploadhouse', methods=['POST'])
def upload_house():
    house_file = request.form
    facility_list = house_file.get_list

    group = house_file.get('area_id')
    room_count = house_file.get('room_count')
    acreage = house_file.get('acreage')
    unit = house_file.get('unit')
    capacity = house_file.get('capacity')
    beds = house_file.get('beds')
    deposit = house_file.get('deposit')
    min_days = house_file.get('min_days')
    max_days = house_file.get('max_days')
    facility = house_file.get('facility')

    house = House()
    house.name = group
    house.room_count = room_count
    house.acreage = acreage
    house.unit = unit
    house.capacity = capacity
    house.beds = beds
    house.deposit = deposit
    house.min_days = min_days
    house.max_days = max_days
    house.name = facility

    try:
        house.add_update()
        return jsonify(status_code.SUCCESS)
    except Exception as e:
        return jsonify(status_code.DATABASE_ERROR)

