from flask import Flask, render_template, url_for, request, redirect, Blueprint
from datetime import datetime

import pandas as pd
import os
import pprint
from loguru import logger
from datetime import datetime as dt



# Blueprint を作成
bp = Blueprint('servomotor_smart_control', __name__)

# /post にアクセスされ、GETもしくはPOSTメソッドでデータが送信された場合の処理
@bp.route('/servomotor_smart_control', methods=['GET', 'POST'])
def servomotor_smart_control():
    
    # --------------------------------------------
    # param setting
    #
    segment = "servomotor_smart_control"
    # running_type = "develop"
    running_type = "master"
    data_path = "apps/static/assets/data/smart_control_data.csv"
    
    # --------------------------------------------
    # make date
    #
    tdatetime = dt.now()
    tstr = tdatetime.strftime('%Y%m%d_%H%M%S')
           
    # --------------------------------------------
    # POSTメソッドの場合
    #
    if request.method == 'POST':

        # convert dict
        dict_form = request.form.to_dict()
        
        # insert date
        dict_form["date"] = tstr
        
        # detect data
        is_file = os.path.isfile(data_path)
        if(is_file):
            df_form = pd.read_csv(data_path, index_col=0)
            df_form = df_form.append(dict_form, ignore_index=True)
        else:
            # pprint.pprint(dict_form)
            df_form = pd.DataFrame(dict_form, index=[0])
        
        # save data
        logger.info("df_form")
        df_form.to_csv(data_path)
        pprint.pprint(df_form)
        
    else:
        df_form = pd.DataFrame({})
    
    # --------------------------------------------
    # convert df to dict
    #
    logger.info("dict_list_form")
    dict_list_form = df_form.to_dict('records')
    pprint.pprint(dict_list_form)
    
    return render_template('smart_control/servomotor_smart_control.html', 
                            dict_list_form=dict_list_form, 
                            segment=segment, 
                            running_type=running_type)