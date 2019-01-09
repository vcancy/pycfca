from .import client


def test_synthesize_template_with_pdfid():
    ret = client.synthesize_template_with_pdfid(
        "5c34b985ff0aa50b26a8ca95",
        "1005",
        "5c34b985ff0aa50b26a8ca95",
        '<FieldList hashAlg="sha1" savedBizXmlId="" savedTimeIncrement="" partialFlattening="false"><Field><FieldId>name</FieldId><FieldValue>陈实实</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>id_card</FieldId><FieldValue>510124198987654436</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>loan_amount</FieldId><FieldValue>1234567.27</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>loan_limit</FieldId><FieldValue>24</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>loan_rate_name</FieldId><FieldValue>年利率</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>loan_start_date</FieldId><FieldValue>2020年10月1日</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>loan_rate</FieldId><FieldValue>0.03</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>payment_account</FieldId><FieldValue>511714199012035562</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>payback_method</FieldId><FieldValue>等额本息</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>due_date</FieldId><FieldValue>1</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>contract_date</FieldId><FieldValue>2018年10月1日</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>contract_no</FieldId><FieldValue>5b9761da829d65a4d64ed5f5</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>contract_no</FieldId><FieldValue>2019010822535768151f839619f2cf</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>loan_amount_upper</FieldId><FieldValue>壹佰贰拾叁万肆仟伍佰陆拾柒圆贰角柒分</FieldValue><FieldType>text</FieldType></Field></FieldList>',
        "XXWJR"
    )
    print(ret.code, ret.msg, ret.data)
    assert ret.code == "200"


def test_synthesize_template_with_pdfid_error():
    ret = client.synthesize_template_with_pdfid(
        "5c34b985ff0aa50b26a8ca95",
        "xxx",
        "5c34b985ff0aa50b26a8ca95",
        '<FieldList hashAlg="sha1" savedBizXmlId="" savedTimeIncrement="" partialFlattening="false"><Field><FieldId>name</FieldId><FieldValue>陈实实</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>id_card</FieldId><FieldValue>510124198987654436</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>loan_amount</FieldId><FieldValue>1234567.27</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>loan_limit</FieldId><FieldValue>24</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>loan_rate_name</FieldId><FieldValue>年利率</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>loan_start_date</FieldId><FieldValue>2020年10月1日</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>loan_rate</FieldId><FieldValue>0.03</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>payment_account</FieldId><FieldValue>511714199012035562</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>payback_method</FieldId><FieldValue>等额本息</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>due_date</FieldId><FieldValue>1</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>contract_date</FieldId><FieldValue>2018年10月1日</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>contract_no</FieldId><FieldValue>5b9761da829d65a4d64ed5f5</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>contract_no</FieldId><FieldValue>2019010822535768151f839619f2cf</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>loan_amount_upper</FieldId><FieldValue>壹佰贰拾叁万肆仟伍佰陆拾柒圆贰角柒分</FieldValue><FieldType>text</FieldType></Field></FieldList>',
        "XXWJR"
    )
    print(ret.code, ret.msg, ret.data)
    assert ret.code != "200"
