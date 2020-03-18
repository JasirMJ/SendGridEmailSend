
import sendgrid
import os
import requests
import json
import base64
import pdfkit


def SendMailWithTemplateIncludingAttachements(tomail):
    SEND_GRID_KEY = YOUR_API_KEY

    items_list = ['computer', 'software service', 'mouse', 'webdevelopement', 'book', 'marker', 'door', 'charger',
                  'table', 'ac', 'tv', 'fan', 'headset', 'pen', 'pencil', 'waterbottle', 'iphone', 'redmi', 'samsung',
                  'nexus', 'bag', 'chair', ]
    items_price = [20000, 35000, 34, 45, 56, 56, 877, 45, 3443, 55, 44, 77, 222, 445, 767, 1234, 122, 111, 455, 444,
                   555, 56, 5788, 123, 43, 534, 234, 234, 234, 23, 423, 4, 234, 234, 23, 534, 2, 5234, 52, 634, 1123,
                   234, 32423, 12543, 123, 123]
    total = 0

    items = "<tr class='heading'> <td> Item </td> <td> Price </td>  </tr>"

    for x in range(1, 10):
        total = total + items_price[x]
        items = items + '<tr class="item"><td>' + items_list[x] + '</td><td>' + str(items_price[x]) + '</td></tr>'

    template = '''

    <!doctype html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>invoice</title>

        <style>
        .invoice-box {
            max-width: 800px;
            margin: auto;
            padding: 30px;
            border: 1px solid #eee;
            box-shadow: 0 0 10px rgba(0, 0, 0, .15);
            font-size: 16px;
            line-height: 24px;
            font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;
            color: #555;
        }

        .invoice-box table {
            width: 100%;
            line-height: inherit;
            text-align: left;
        }

        .invoice-box table td {
            padding: 5px;
            vertical-align: top;
        }

        .invoice-box table tr td:nth-child(2) {
            text-align: right;
        }

        .invoice-box table tr.top table td {
            padding-bottom: 20px;
        }

        .invoice-box table tr.top table td.title {
            font-size: 45px;
            line-height: 45px;
            color: #333;
        }

        .invoice-box table tr.information table td {
            padding-bottom: 40px;
        }

        .invoice-box table tr.heading td {
            background: #eee;
            border-bottom: 1px solid #ddd;
            font-weight: bold;
        }

        .invoice-box table tr.details td {
            padding-bottom: 20px;
        }

        .invoice-box table tr.item td{
            border-bottom: 1px solid #eee;
        }

        .invoice-box table tr.item.last td {
            border-bottom: none;
        }

        .invoice-box table tr.total td:nth-child(2) {
            border-top: 2px solid #eee;
            font-weight: bold;
        }

        @media only screen and (max-width: 600px) {
            .invoice-box table tr.top table td {
                width: 100%;
                display: block;
                text-align: center;
            }

            .invoice-box table tr.information table td {
                width: 100%;
                display: block;
                text-align: center;
            }
        }

        /** RTL **/
        .rtl {
            direction: rtl;
            font-family: Tahoma, 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;
        }

        .rtl table {
            text-align: right;
        }

        .rtl table tr td:nth-child(2) {
            text-align: left;
        }
        </style>
    </head>

    <body>
        <div class="invoice-box">
            <table cellpadding="0" cellspacing="0">
                <tr class="top">
                    <td colspan="2">
                        <table>
                            <tr>
                                <td class="title">
                                    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTK4yHZUTNYyi-TEiXhxOy6TVF8CwMCvX9IiGp0Ta1aGyhuboYe&s" style="width:100px; max-width:300px;">
                                </td>
                                <td>
                                    Invoice #: [invoicenumber]<br>
                                    Created: [create date]<br>
                                    Due: [due date]
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
                <tr class="information">
                    <td colspan="2">
                        <table>
                            <tr>
                                <td>
                                    Codedady Solutions.<br>
                                    Malappuram <br>
                                    Perinthalmanna, 679321
                                </td>
                                <td>
                                    LIFOC Corp.<br>
                                    Mohamed Jasir K P<br>
                                    jasirmj@gmail.com
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
                <tr class="heading">
                    <td>
                        Payment Method
                    </td>
                    <td>
                        Check #
                    </td>
                </tr>
                <tr class="details">
                    <td>
                        Check
                    </td>
                    <td>
                        1000
                    </td>
                </tr>
                ''' + items + '''
                <tr class="total">
                    <td></td>
                    <td>
                       Total: &#x20b9;''' + str(total) + '''
                    </td>
                </tr>
            </table>
        </div>
    </body>
    </html>
    '''

    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

    pdfkit.from_string(template, 'jasir1.pdf', configuration=config)  # Generate pdf

    # cwd = os.getcwd()  # Get the current working directory (cwd)
    # files = os.listdir(cwd)  # Get all the files in that directory
    # print("Files in %r: %s" % (cwd, files))

    file_path = 'jasir1.pdf'
    with open(file_path, 'rb') as f:
        data = f.read()
        f.close()
    encoded = base64.b64encode(data).decode()

    sg = sendgrid.SendGridAPIClient(api_key=SEND_GRID_KEY)
    data = {
      "personalizations": [
        {
          "to": [
            {
              "email": tomail
            }
          ],
          "subject": "Sending with SendGrid is Fun"
        }
      ],
      "from": {
        "email": "test@example.com"
      },
        "attachments": [
            {
                "content": encoded,
                "content_id": "ii_139db99fdb5c3704",
                "disposition": "inline",
                "filename": "jasir1.pdf",
                "name": "jasir1",
                "type": "pdf"
            }
        ],
      "content": [
        {
          "type": "html/css",
          "value": template
        }
      ]
    }
    response = sg.client.mail.send.post(request_body=data)
    print(response.status_code)
    # print(response.body)
    # print(response.headers)

SendMailWithTemplateIncludingAttachements("toemail@gmail.com")
