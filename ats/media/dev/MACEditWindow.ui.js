/*
 * File: MACEditWindow.ui.js
 * Date: Wed Jun 01 2011 08:49:10 GMT-0400 (EDT)
 * 
 * This file was generated by Ext Designer version xds-1.0.2.14.
 * http://www.extjs.com/products/designer/
 *
 * This file will be auto-generated each and everytime you export.
 *
 * Do NOT hand edit this file.
 */

MACEditWindowUi = Ext.extend(Ext.Window, {
    title: 'Edit Event',
    width: 800,
    layout: 'fit',
    autoHeight: true,
    collapsible: true,
    initHidden: false,
    hideBorders: true,
    initComponent: function() {
        this.items = [
            {
                xtype: 'maceditform'
            }
        ];
        MACEditWindowUi.superclass.initComponent.call(this);
    }
});