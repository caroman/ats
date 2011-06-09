/*
 * File: CandidateMACGrid.ui.js
 * Date: Thu Jun 09 2011 08:24:48 GMT-0400 (EDT)
 * 
 * This file was generated by Ext Designer version xds-1.0.2.14.
 * http://www.extjs.com/products/designer/
 *
 * This file will be auto-generated each and everytime you export.
 *
 * Do NOT hand edit this file.
 */

CandidateMACGridUi = Ext.extend(Ext.grid.GridPanel, {
    store: 'CandidateMACsStore',
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
                header: 'Mandate',
                sortable: true,
                width: 100,
                dataIndex: 'mandate',
                id: 'mandate__title'
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
            store: 'CandidateMACsStore',
            buttonAlign: 'right',
            displayInfo: true
        };
        this.view = Ext.create({
            xtype: 'candidatemacgridview'
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
        CandidateMACGridUi.superclass.initComponent.call(this);
    }
});
