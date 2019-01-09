from .import client


def test_compound_signature_auto_pdf():
    ret = client.synthesize_template_with_pdfid(
        "5c34bad8ff0aa50c39d7dc66",
        "1005",
        "5c34bad8ff0aa50c39d7dc66",
        '<FieldList hashAlg="sha1" savedBizXmlId="" savedTimeIncrement="" partialFlattening="false"><Field><FieldId>name</FieldId><FieldValue>陈实实</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>id_card</FieldId><FieldValue>510124198987654436</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>loan_amount</FieldId><FieldValue>1234567.27</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>loan_limit</FieldId><FieldValue>24</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>loan_rate_name</FieldId><FieldValue>年利率</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>loan_start_date</FieldId><FieldValue>2020年10月1日</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>loan_rate</FieldId><FieldValue>0.03</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>payment_account</FieldId><FieldValue>511714199012035562</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>payback_method</FieldId><FieldValue>等额本息</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>due_date</FieldId><FieldValue>1</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>contract_date</FieldId><FieldValue>2018年10月1日</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>contract_no</FieldId><FieldValue>5b9761da829d65a4d64ed5f5</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>contract_no</FieldId><FieldValue>2019010822535768151f839619f2cf</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>loan_amount_upper</FieldId><FieldValue>壹佰贰拾叁万肆仟伍佰陆拾柒圆贰角柒分</FieldValue><FieldType>text</FieldType></Field></FieldList>',
        "XXWJR"
    )
    ret = client.compound_signature_auto_pdf(
        "5c34bad8ff0aa50c39d7dc66",
        "<PdfBean><PdfId>5c34bad8ff0aa50c39d7dc66</PdfId><BizSerialNo>5c34bad8ff0aa50c39d7dc66</BizSerialNo><OutputFilePath>/data/5c34bad8ff0aa50c39d7dc66.pdf</OutputFilePath><ReturnPdfOrNot>true</ReturnPdfOrNot></PdfBean>'",
        [],
        '<List><Request><SealCode>00000005</SealCode><SealPassword>123456</SealPassword><Type>2</Type><LX>1</LX><LY>1</LY><Keyword></Keyword><KeywordPositionIndex></KeywordPositionIndex><LocationStyle></LocationStyle><Page>1</Page><OffsetX></OffsetX><OffsetY></OffsetY><LocationCode></LocationCode><Visible>true</Visible><SealPerson></SealPerson><SealLocation></SealLocation><SealReason></SealReason><SealImageSize>100</SealImageSize></Request><Request><SealImageSize>50</SealImageSize><HandwritingImage></HandwritingImage><SealLayer2Text>陈实实</SealLayer2Text><SealLayer2TextStyle>font-size:16;font-color:000000;width:100;</SealLayer2TextStyle><SealPerson>陈实实</SealPerson><IdentificationType>0</IdentificationType><IdentificationNo>511714199012035562</IdentificationNo><PhoneNo>18180414778</PhoneNo><SealLocation></SealLocation><SealReason></SealReason><KeyAlg></KeyAlg><Visible>true</Visible><Type>2</Type><Page>1</Page><LX>1</LX><LY>1</LY><Keyword></Keyword><KeywordPositionIndex></KeywordPositionIndex><LocationStyle></LocationStyle><OffsetX></OffsetX><OffsetY></OffsetY><LocationCode></LocationCode><ProofHashXml></ProofHashXml></Request></List>',
        "XXWJR"
    )
    print(ret.code, ret.msg)
    assert ret.code == "200"


def test_compound_signature_auto_pdf_error():
    ret = client.synthesize_template_with_pdfid(
        "5c34bad8ff0aa50c39d7dc66",
        "1005",
        "5c34bad8ff0aa50c39d7dc66",
        '<FieldList hashAlg="sha1" savedBizXmlId="" savedTimeIncrement="" partialFlattening="false"><Field><FieldId>name</FieldId><FieldValue>陈实实</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>id_card</FieldId><FieldValue>510124198987654436</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>loan_amount</FieldId><FieldValue>1234567.27</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>loan_limit</FieldId><FieldValue>24</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>loan_rate_name</FieldId><FieldValue>年利率</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>loan_start_date</FieldId><FieldValue>2020年10月1日</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>loan_rate</FieldId><FieldValue>0.03</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>payment_account</FieldId><FieldValue>511714199012035562</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>payback_method</FieldId><FieldValue>等额本息</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>due_date</FieldId><FieldValue>1</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>contract_date</FieldId><FieldValue>2018年10月1日</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>contract_no</FieldId><FieldValue>5b9761da829d65a4d64ed5f5</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>contract_no</FieldId><FieldValue>2019010822535768151f839619f2cf</FieldValue><FieldType>text</FieldType></Field><Field><FieldId>loan_amount_upper</FieldId><FieldValue>壹佰贰拾叁万肆仟伍佰陆拾柒圆贰角柒分</FieldValue><FieldType>text</FieldType></Field></FieldList>',
        "XXWJR"
    )
    ret = client.compound_signature_auto_pdf(
        "5c34bad8ff0aa50c39d7dc66",
        "<PdfBean><PdfId>5c34bad8ff0aa50c39d7dc66</PdfId><BizSerialNo>5c34bad8ff0aa50c39d7dc66</BizSerialNo><OutputFilePath>/data/5c34bad8ff0aa50c39d7dc66.pdf</OutputFilePath><ReturnPdfOrNot>true</ReturnPdfOrNot></PdfBean>'",
        [],
        '<List><Request><SealCode>00000005</SealCode><SealPassword>123456</SealPassword><Type>2</Type><LX>1</LX><LY>1</LY><Keyword></Keyword><KeywordPositionIndex></KeywordPositionIndex><LocationStyle></LocationStyle><Page>1</Page><OffsetX></OffsetX><OffsetY></OffsetY><LocationCode></LocationCode><Visible>true</Visible><SealPerson></SealPerson><SealLocation></SealLocation><SealReason></SealReason><SealImageSize>100</SealImageSize></Request><Request><SealImageSize>50</SealImageSize><HandwritingImage></HandwritingImage><SealLayer2Text>陈实实</SealLayer2Text><SealLayer2TextStyle>font-size:16;font-color:000000;width:100;</SealLayer2TextStyle><SealPerson>陈实实</SealPerson><IdentificationType>0</IdentificationType><IdentificationNo>511714199012035562</IdentificationNo><PhoneNo>18180414778</PhoneNo><SealLocation></SealLocation><SealReason></SealReason><KeyAlg></KeyAlg><Visible>true</Visible><Type>2</Type><Page>1</Page><LX>1</LX><LY>1</LY><Keyword></Keyword><KeywordPositionIndex></KeywordPositionIndex><LocationStyle></LocationStyle><OffsetX></OffsetX><OffsetY></OffsetY><LocationCode></LocationCode><ProofHashXml></ProofHashXml></Request></List>',
        "XXWJR1"
    )
    print(ret.code, ret.msg)
    assert ret.code != "200"
