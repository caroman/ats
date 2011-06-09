/*
 * File: ATS.ui.js
 * Date: Thu Jun 09 2011 08:24:47 GMT-0400 (EDT)
 * 
 * This file was generated by Ext Designer version xds-1.0.2.14.
 * http://www.extjs.com/products/designer/
 *
 * This file will be auto-generated each and everytime you export.
 *
 * Do NOT hand edit this file.
 */

ATSUi = Ext.extend(Ext.Viewport, {
    layout: 'border',
    id: 'ATSViewport',
    initComponent: function() {
        this.items = [
            {
                xtype: 'panel',
                region: 'north',
                width: 100,
                tbar: {
                    xtype: 'toolbar',
                    items: [
                        {
                            xtype: 'displayfield',
                            value: 'Applicant Tracking System',
                            submitValue: false
                        },
                        {
                            xtype: 'tbfill'
                        },
                        {
                            xtype: 'button',
                            text: 'Logout',
                            height: 50,
                            width: 100,
                            scale: 'large',
                            iconCls: 'img_logout',
                            ref: '../../logoutButton'
                        }
                    ]
                }
            },
            {
                xtype: 'panel',
                region: 'center',
                layout: 'border',
                border: false,
                hideBorders: true,
                items: [
                    {
                        region: 'center',
                        xtype: 'maintabpanel'
                    }
                ]
            }
        ];
        ATSUi.superclass.initComponent.call(this);
    }
});
