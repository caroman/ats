/*
 * File: CandidateGrid.ui.js
 * Date: Thu Jun 09 2011 08:24:48 GMT-0400 (EDT)
 * 
 * This file was generated by Ext Designer version xds-1.0.2.14.
 * http://www.extjs.com/products/designer/
 *
 * This file will be auto-generated each and everytime you export.
 *
 * Do NOT hand edit this file.
 */

CandidateGridUi = Ext.extend(Ext.grid.GridPanel, {
    store: 'CandidateStore',
    stripeRows: true,
    autoShow: true,
    border: false,
    hideBorders: true,
    initComponent: function() {
        this.selModel = new Ext.grid.RowSelectionModel({
            singleSelect: true
        });
        this.columns = [
            {
                xtype: 'gridcolumn',
                dataIndex: 'id',
                header: 'Candidate',
                sortable: true,
                width: 60,
                tooltip: 'Candidate ID',
                fixed: true,
                id: 'id'
            },
            {
                xtype: 'gridcolumn',
                header: 'First Name',
                sortable: true,
                width: 100,
                dataIndex: 'first_name',
                id: 'first_name'
            },
            {
                xtype: 'gridcolumn',
                header: 'Last Name',
                sortable: true,
                width: 100,
                dataIndex: 'last_name',
                id: 'last_name'
            },
            {
                xtype: 'gridcolumn',
                header: 'Phone',
                sortable: true,
                width: 100,
                dataIndex: 'phone',
                fixed: true,
                id: 'phone'
            },
            {
                xtype: 'gridcolumn',
                header: 'Ph Ext',
                sortable: true,
                width: 50,
                dataIndex: 'phone_extension',
                tooltip: 'Phone Extension',
                fixed: true,
                id: 'phone_extension'
            },
            {
                xtype: 'gridcolumn',
                header: 'Mobile',
                sortable: true,
                width: 100,
                dataIndex: 'mobile',
                id: 'mobile'
            },
            {
                xtype: 'gridcolumn',
                header: 'EMail 1',
                sortable: true,
                width: 100,
                dataIndex: 'email_1',
                id: 'email1'
            },
            {
                xtype: 'gridcolumn',
                header: 'Recruiter',
                sortable: true,
                width: 70,
                dataIndex: 'created_by__username',
                fixed: true,
                id: 'created_by__username'
            }
        ];
        this.tbar = {
            xtype: 'toolbar',
            items: [
                {
                    xtype: 'button',
                    text: 'New',
                    iconCls: 'img_add_candidate',
                    scale: 'medium',
                    tooltip: 'Create a new candidate',
                    ref: '../newbutton'
                },
                {
                    xtype: 'button',
                    text: 'Add Event',
                    tooltip: 'Add event to selected candidate',
                    iconCls: 'img_add_event',
                    scale: 'medium',
                    ref: '../addmacbutton'
                },
                {
                    xtype: 'button',
                    text: 'Events',
                    tooltip: 'Show events for the selected candidate',
                    iconCls: 'img_list_events',
                    scale: 'medium',
                    ref: '../macsbutton'
                },
                {
                    xtype: 'button',
                    text: 'Mandates',
                    tooltip: 'Show mandates for the selected candidate',
                    iconCls: 'img_list_mandates',
                    scale: 'medium',
                    ref: '../mandatesbutton'
                }
            ]
        };
        this.bbar = {
            xtype: 'toolbar',
            buttonAlign: 'right',
            items: [
                {
                    xtype: 'paging',
                    store: 'CandidateStore',
                    pageSize: 15,
                    hideBorders: true,
                    autoHeight: true,
                    displayInfo: true,
                    buttonAlign: 'right',
                    ref: '../pagingtoolbar'
                }
            ]
        };
        this.view = new Ext.grid.GridView({
            forceFit: true
        });
        CandidateGridUi.superclass.initComponent.call(this);
    }
});
