/*
 * File: MandateClass.ui.js
 * Date: Thu Jun 09 2011 08:24:48 GMT-0400 (EDT)
 * 
 * This file was generated by Ext Designer version xds-1.0.2.14.
 * http://www.extjs.com/products/designer/
 *
 * This file will be auto-generated each and everytime you export.
 *
 * Do NOT hand edit this file.
 */

MandateClassUi = Ext.extend(Ext.Panel, {
    title: 'Mandates',
    width: 576,
    layout: 'border',
    hideBorders: true,
    initComponent: function() {
        this.items = [
            {
                xtype: 'panel',
                region: 'center',
                layout: 'border',
                hideBorders: true,
                items: [
                    {
                        region: 'center',
                        ref: '../grid',
                        xtype: 'mandategrid'
                    },
                    {
                        xtype: 'panel',
                        region: 'south',
                        width: 250,
                        collapsible: true,
                        floatable: false,
                        split: true,
                        titleCollapse: true,
                        layout: 'fit',
                        hideBorders: true,
                        border: false,
                        height: 250,
                        items: [
                            {
                                xtype: 'tabpanel',
                                activeTab: 0,
                                border: false,
                                hideBorders: true,
                                deferredRender: false,
                                items: [
                                    {
                                        xtype: 'panel',
                                        title: 'Administration',
                                        layout: 'fit',
                                        frame: true,
                                        autoScroll: true,
                                        border: false,
                                        items: [
                                            {
                                                ref: '../../../../mandateclosingform',
                                                xtype: 'mandateclosingform'
                                            }
                                        ]
                                    },
                                    {
                                        xtype: 'panel',
                                        title: 'Events',
                                        layout: 'fit',
                                        hideBorders: true,
                                        border: false,
                                        items: [
                                            {
                                                ref: '../../../../macgrid',
                                                xtype: 'mandatemacgrid'
                                            }
                                        ]
                                    },
                                    {
                                        xtype: 'panel',
                                        title: 'Mandate',
                                        layout: 'fit',
                                        frame: true,
                                        autoScroll: true,
                                        border: false,
                                        items: [
                                            {
                                                ref: '../../../../mandateeditform',
                                                xtype: 'mandateeditform'
                                            }
                                        ]
                                    },
                                    {
                                        xtype: 'panel',
                                        title: 'Responsability',
                                        autoScroll: true,
                                        hideBorders: true,
                                        border: false,
                                        layout: 'fit',
                                        items: [
                                            {
                                                ref: '../../../../mandateresponsabilityform',
                                                xtype: 'mandateeditdescresponsabilityform'
                                            }
                                        ]
                                    },
                                    {
                                        xtype: 'panel',
                                        title: 'Requirement',
                                        autoScroll: true,
                                        hideBorders: true,
                                        border: false,
                                        layout: 'fit',
                                        items: [
                                            {
                                                ref: '../../../../mandaterequirementform',
                                                xtype: 'mandateeditdescrequirementform'
                                            }
                                        ]
                                    },
                                    {
                                        xtype: 'panel',
                                        title: 'Candidates',
                                        layout: 'fit',
                                        hideBorders: true,
                                        border: false,
                                        items: [
                                            {
                                                xtype: 'grid',
                                                store: 'MandateCandidatesStore',
                                                stripeRows: true,
                                                hideBorders: true,
                                                border: false,
                                                ref: '../../../../candidatesgrid',
                                                columns: [
                                                    {
                                                        xtype: 'gridcolumn',
                                                        header: 'First Name',
                                                        sortable: true,
                                                        width: 100,
                                                        dataIndex: 'first_name'
                                                    },
                                                    {
                                                        xtype: 'gridcolumn',
                                                        header: 'Last Name',
                                                        sortable: true,
                                                        width: 100,
                                                        dataIndex: 'last_name'
                                                    },
                                                    {
                                                        xtype: 'gridcolumn',
                                                        header: 'Phone',
                                                        sortable: true,
                                                        width: 100,
                                                        dataIndex: 'phone'
                                                    }
                                                ],
                                                bbar: {
                                                    xtype: 'paging',
                                                    store: 'MandateCandidatesStore',
                                                    buttonAlign: 'right'
                                                },
                                                view: new Ext.grid.GridView({
                                                    forceFit: true
                                                })
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            {
                xtype: 'panel',
                width: 400,
                height: 250,
                region: 'east',
                tpl: [

                ],
                collapsible: true,
                split: true,
                hideBorders: true,
                border: false,
                autoScroll: true,
                ref: 'infopanel'
            }
        ];
        MandateClassUi.superclass.initComponent.call(this);
    }
});
