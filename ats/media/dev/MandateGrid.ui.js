/*
 * File: MandateGrid.ui.js
 * Date: Thu Jun 09 2011 08:24:48 GMT-0400 (EDT)
 * 
 * This file was generated by Ext Designer version xds-1.0.2.14.
 * http://www.extjs.com/products/designer/
 *
 * This file will be auto-generated each and everytime you export.
 *
 * Do NOT hand edit this file.
 */

MandateGridUi = Ext.extend(Ext.grid.GridPanel, {
    store: 'MandateStore',
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
                header: 'Mandate',
                sortable: true,
                width: 60,
                tooltip: 'Candidate ID',
                fixed: true
            },
            {
                xtype: 'gridcolumn',
                dataIndex: 'title',
                header: 'Title',
                sortable: true,
                width: 100
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
                header: 'Candidates',
                sortable: true,
                width: 70,
                dataIndex: 'candidate_count',
                fixed: true
            },
            {
                xtype: 'datecolumn',
                header: 'Post End',
                sortable: true,
                width: 75,
                dataIndex: 'posting_end_date',
                format: 'Y-m-d',
                fixed: true
            },
            {
                xtype: 'gridcolumn',
                header: 'Hiring Manager',
                sortable: true,
                width: 100,
                dataIndex: 'hiring_manager',
                id: 'hiring_manager__name'
            },
            {
                xtype: 'gridcolumn',
                header: 'Recruiter',
                sortable: true,
                width: 70,
                dataIndex: 'created_by__username',
                fixed: true
            }
        ];
        this.tbar = {
            xtype: 'toolbar',
            items: [
                {
                    xtype: 'button',
                    text: 'New',
                    iconCls: 'img_add_mandate',
                    scale: 'medium',
                    tooltip: 'Add a new mandate',
                    ref: '../newbutton'
                },
                {
                    xtype: 'button',
                    text: 'Add Event',
                    tooltip: 'Show MACs for the selected candidate',
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
                    text: 'Candidates',
                    tooltip: 'Show candidates for the selected candidate',
                    iconCls: 'img_list_candidates',
                    scale: 'medium',
                    ref: '../candidatesbutton'
                }
            ]
        };
        this.bbar = {
            xtype: 'toolbar',
            buttonAlign: 'right',
            items: [
                {
                    xtype: 'paging',
                    store: 'MandateStore',
                    pageSize: 15,
                    hideBorders: true,
                    displayInfo: true,
                    buttonAlign: 'right',
                    ref: '../pagingtoolbar'
                }
            ]
        };
        this.view = Ext.create({
            xtype: 'mandategridview'
        });
        MandateGridUi.superclass.initComponent.call(this);
    }
});
