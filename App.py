from flask import Flask, render_template, request, flash

app = Flask(__name__)


app.secret_key = 'a5288a57111b35f98fc47e58a083106476808dd0a206f41c'

output = 'M2012'
slices_ID = [
        'M201200', 'M201201', 'M201203', 'M201204', 'M201205', 'M201206',
        'M201207', 'M201208', 'M201209', 'M201210', 'M201211', 'M201212',
        'M201213', 'M201214', 'M201215', 'M201216', 'M201217', 'M201219',
        'M201220', 'M201221', 'M201222', 'M201225', 'M201226', 'M201227',
        'M201228', 'M201230', 'M201232', 'M201235', 'M201237'
        ]  
    # Assuming you meant to define the slices_ID list

items_ID = [
        'M502000', 'M502001', 'M502002', 'M502003', 'M502004', 'M502005',
        'M502006', 'M502007', 'M502008', 'M502009', 'M502010', 'M502011',
        'M502012', 'M502013', 'M502014', 'M502015', 'M502016', 'M502017',
        'M502018', 'M502019', 'M502020', 'M502021', 'M502022', 'M502023',
        'M502024', 'M502025', 'M502026', 'M502027', 'M502028', 'M502029',
        'M502030', 'M502031', 'M502032', 'M502033', 'M502034', 'M502035',
        'M502036', 'M502037', 'M502038', 'M502039', 'M502040', 'M502041',
        'M502042', 'M502043', 'M502044', 'M502045', 'M502046', 'M502047',
        'M502048', 'M502049', 'M502050', 'M502051', 'M502052', 'M502053',
        'M502054', 'M502055', 'M502056', 'M502057', 'M502058', 'M502059',
        'M502060', 'M502061', 'M502062', 'M502063', 'M502064', 'M502065',
        'M502066', 'M502067', 'M502068', 'M502069', 'M502070', 'M502071',
        'M502072', 'M502073', 'M502074', 'M502075', 'M502076', 'M502077',
        'M502078', 'M502079', 'M502080', 'M502081', 'M502082', 'M502083',
        'M502084', 'M502085', 'M502086', 'M502087', 'M502088', 'M502089',
        'M502090', 'M502091', 'M502092', 'M502093', 'M502094', 'M502095',
        'M502096', 'M502097', 'M502098', 'M502099', 'M502100', 'M502101',
        'M502102', 'M502103', 'M502104', 'M502105', 'M502106', 'M502107',
        'M502108', 'M502109', 'M502110', 'M502111', 'M502112', 'M502113',
        'M502114', 'M502115', 'M502116', 'M502117', 'M502118', 'M502119',
        'M502120', 'M502121', 'M502122', 'M502123', 'M502124', 'M502125',
        'M502126', 'M502127', 'M502128', 'M502129', 'M502130', 'M502131',
        'M502132', 'M502133', 'M502134', 'M502135', 'M502136', 'M502137',
        'M502138', 'M502139', 'M502140', 'M502141', 'M502142', 'M502143',
        'M502144', 'M502145', 'M502146', 'M502147', 'M502148', 'M502149',
        'M502150', 'M502151', 'M502152', 'M502153', 'M502154', 'M502155',
        'M502156', 'M502157', 'M502158', 'M502159', 'M502160', 'M502161',
        'M502162', 'M502163', 'M502164', 'M502165', 'M502166', 'M502167',
        'M502168', 'M502169', 'M502170', 'M502171', 'M502172', 'M502173',
        'M502174', 'M502175', 'M502176', 'M502177', 'M502178', 'M502179',
        'M502180', 'M502181', 'M502182', 'M502183', 'M502184', 'M502185',
        'M502186', 'M502187', 'M502188', 'M502189', 'M502190', 'M502191',
        'M502192', 'M502193', 'M502194', 'M502195', 'M502196', 'M502197',
        'M502198', 'M502199', 'M502200', 'M502201', 'M502202', 'M502203',
        'M502204', 'M502205', 'M502206', 'M502207', 'M502208', 'M502209',
        'M502210', 'M502211', 'M502212', 'M502213', 'M502214', 'M502215',
        'M502216', 'M502217', 'M502218', 'M502219', 'M502220', 'M502221',
        'M502222', 'M502223', 'M502224', 'M502225', 'M502226', 'M502227'
    ]


options = {
        slices_ID[0]: [items_ID[0], items_ID[2], items_ID[5], items_ID[8], items_ID[82], items_ID[83],
                       items_ID[84], items_ID[85], items_ID[208], items_ID[209], items_ID[210], items_ID[211]],
        
        slices_ID[1]: [items_ID[1], items_ID[3]],
        
        slices_ID[2]: [items_ID[10], items_ID[12], items_ID[13], items_ID[15], items_ID[16], items_ID[18],
                        items_ID[21], items_ID[22], items_ID[24], items_ID[26], items_ID[27], items_ID[29]],
        
        slices_ID[3]: [items_ID[11], items_ID[14], items_ID[17], items_ID[19], items_ID[62], items_ID[63],
                    items_ID[86], items_ID[87], items_ID[88], items_ID[89], items_ID[148], items_ID[150],
                    items_ID[174]],
        
        slices_ID[4]: [items_ID[30], items_ID[31], items_ID[58], items_ID[59], items_ID[66], items_ID[67],
                    items_ID[68], items_ID[69], items_ID[70], items_ID[71], items_ID[72], items_ID[73],
                    items_ID[120], items_ID[121], items_ID[124], items_ID[125], items_ID[163], items_ID[165],
                    items_ID[200], items_ID[201], items_ID[220], items_ID[221], items_ID[224], items_ID[225]],
        
        slices_ID[5]: [items_ID[32], items_ID[33], items_ID[34], items_ID[35], items_ID[48], items_ID[49],
                    items_ID[52], items_ID[53], items_ID[198], items_ID[199]],
        
        slices_ID[6]: [items_ID[36], items_ID[37], items_ID[38], items_ID[39], items_ID[46], items_ID[47],
                    items_ID[50], items_ID[51], items_ID[54], items_ID[55], items_ID[80], items_ID[81],
                    items_ID[106], items_ID[107], items_ID[108], items_ID[109], items_ID[161], items_ID[162],
                    items_ID[186], items_ID[187], items_ID[196], items_ID[197], items_ID[202], items_ID[203],
                    items_ID[206], items_ID[207], items_ID[212], items_ID[213], items_ID[214], items_ID[215],
                    items_ID[216], items_ID[217]],
    
        slices_ID[7]: [items_ID[40], items_ID[41]],
        
        slices_ID[8]: [items_ID[42], items_ID[43], items_ID[104], items_ID[105], items_ID[218], items_ID[219],
                    items_ID[222], items_ID[223]],
        
        slices_ID[9]: [items_ID[44], items_ID[45], items_ID[98], items_ID[99], items_ID[100], items_ID[101],
                    items_ID[102], items_ID[103], items_ID[180], items_ID[181], items_ID[182], items_ID[183],
                    items_ID[184], items_ID[185], items_ID[194], items_ID[195]],
        
        slices_ID[10]: [items_ID[64], items_ID[65], items_ID[90], items_ID[91], items_ID[92], items_ID[93],
                    items_ID[94], items_ID[95], items_ID[96], items_ID[97], items_ID[112], items_ID[113],
                    items_ID[114], items_ID[115], items_ID[116], items_ID[117]],
        
        slices_ID[11]: [items_ID[74], items_ID[75], items_ID[78], items_ID[79], items_ID[110], items_ID[111]],
        
        slices_ID[12]: [items_ID[118], items_ID[119]],
        
        slices_ID[13]: [items_ID[4], items_ID[6], items_ID[7], items_ID[9], items_ID[20], items_ID[23],
                    items_ID[25], items_ID[28], items_ID[56], items_ID[57], items_ID[60], items_ID[61],
                    items_ID[76], items_ID[77], items_ID[122], items_ID[123], items_ID[126], items_ID[127],
                    items_ID[128], items_ID[129], items_ID[130], items_ID[131], items_ID[132], items_ID[133],
                    items_ID[134], items_ID[136], items_ID[140], items_ID[142], items_ID[145], items_ID[147],
                    items_ID[173], items_ID[176], items_ID[177], items_ID[178], items_ID[179]],
        
        slices_ID[14]: [items_ID[135], items_ID[137]],
        
        slices_ID[15]: [items_ID[138], items_ID[139]],
        
        slices_ID[16]: [items_ID[141], items_ID[143], items_ID[175]],
        
        slices_ID[17]: [items_ID[149], items_ID[157], items_ID[159]],
        
        slices_ID[18]: [items_ID[151], items_ID[153], items_ID[154], items_ID[156]],
        
        slices_ID[19]: [items_ID[152], items_ID[155]],
        
        slices_ID[20]: [items_ID[158], items_ID[160], items_ID[188], items_ID[189]],
        
        slices_ID[21]: [items_ID[164], items_ID[166]],
        
        slices_ID[22]: [items_ID[167], items_ID[168]],
        
        slices_ID[23]: [items_ID[169], items_ID[170]],
        
        slices_ID[24]: [items_ID[171], items_ID[172]],
        
        slices_ID[25]: [items_ID[190], items_ID[191], items_ID[192], items_ID[193]],
        
        slices_ID[26]: [items_ID[204], items_ID[205]],
        
        slices_ID[27]: [items_ID[226], items_ID[227]],
        
        slices_ID[28]: [items_ID[144], items_ID[146]],
        
    }
    
@app.route('/hex')
def index():
    flash("Articles")
    return render_template("index.html")

@app.route("/process_input", methods=["POST", "GET"])
def process_input():
    slices_Article = request.form.get("user_input")
    if slices_Article in slices_ID:
        items = options[slices_Article]
        flash('Pieces Article, slice ' + slices_Article)
        flash(items)
        return render_template("index.html")
    else:
        flash('Item not found!!!')
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)


