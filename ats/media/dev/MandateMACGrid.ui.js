/*
 * File: MandateMACGrid.ui.js
 * Date: Thu Jun 09 2011 08:24:48 GMT-0400 (EDT)
 * 
 * This file was generated by Ext Designer version xds-1.0.2.14.
 * http://www.extjs.com/products/designer/
 *
 * This file will be auto-generated each and everytime you export.
 *
 * Do NOT hand edit this file.
 */

MandateMACGridUi = Ext.extend(Ext.grid.GridPanel, {
    store: 'MandateMACsStore',
    stripeRows: true,
    hideBorders: true,
    border: false,
    initComponent: function() {
        this.columns = [
            {
                xtype: 'datecolumn',
                header: 'Date',
                sortable: true,
                width: 75,
                dataIndex: 'date',
                format: 'Y-m-d',
                fixed: true
            },
            {
                xtype: 'gridcolumn',
                header: 'Activity',
                sortable: true,
                width: 100,
                dataIndex: 'activity',
                id: 'activity__title'
            },
            {
                xtype: 'gridcolumn',
                header: 'First Name',
                sortable: true,
                width: 100,
                dataIndex: 'candidate',
                id: 'candidate__first_name'
            },
            {
                xtype: 'gridcolumn',
                header: 'Last Name',
                sortable: true,
                width: 100,
                dataIndex: 'candidate',
                id: 'candidate__last_name'
            },
            {
                xtype: 'gridcolumn',
                header: 'Status',
                sortable: true,
                width: 100,
                dataIndex: 'status',
                id: 'status__title'
            },
            {
                xtype: 'gridcolumn',
                header: 'Description',
                sortable: true,
                width: 200,
                dataIndex: 'description'
            }
        ];
        this.bbar = {
            xtype: 'paging',
            store: 'MandateMACsStore',
            buttonAlign: 'right',
            displayInfo: true
        };
        this.view = Ext.create({
            xtype: 'mandatemacgridview'
        });
        this.tbar = {
            xtype: 'toolbar',
            items: [
                {
                    xtype: 'button',
                    text: 'Add Event',
                    tooltip: 'Add event to selected candidate',
                    iconCls: 'img_add',
                    ref: '../newbutton'
                },
                {
                    xtype: 'button',
                    text: 'Edit Event',
                    tooltip: 'Edit selected event',
                    iconCls: 'img_edit_small',
                    ref: '../editbutton'
                }
            ]
        };
        MandateMACGridUi.superclass.initComponent.call(this);
    }
});
