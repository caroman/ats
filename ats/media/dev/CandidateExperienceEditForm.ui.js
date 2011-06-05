/*
 * File: CandidateExperienceEditForm.ui.js
 * Date: Wed Jun 01 2011 08:49:10 GMT-0400 (EDT)
 * 
 * This file was generated by Ext Designer version xds-1.0.2.14.
 * http://www.extjs.com/products/designer/
 *
 * This file will be auto-generated each and everytime you export.
 *
 * Do NOT hand edit this file.
 */

CandidateExperienceEditFormUi = Ext.extend(Ext.form.FormPanel, {
    autoHeight: true,
    padding: '0 50  0 5',
    border: false,
    animCollapse: false,
    hideBorders: true,
    autoWidth: true,
    initComponent: function() {
        this.items = [
            {
                xtype: 'hidden',
                fieldLabel: 'Label',
                name: 'id'
            },
            {
                xtype: 'compositefield',
                fieldLabel: 'Managment Experience',
                items: [
                    {
                        xtype: 'combo',
                        name: 'managment_experience',
                        store: 'ManagmentExperienceStore',
                        valueField: 'id',
                        displayField: 'title',
                        forceSelection: true,
                        hiddenName: 'managment_experience',
                        mode: 'local',
                        triggerAction: 'all',
                        typeAhead: true,
                        flex: 2
                    },
                    {
                        xtype: 'displayfield',
                        value: 'Salary'
                    },
                    {
                        xtype: 'numberfield',
                        name: 'salary',
                        flex: 1,
                        fieldLabel: 'Label'
                    }
                ]
            },
            {
                xtype: 'compositefield',
                fieldLabel: 'Keywords',
                anchor: '100%',
                items: [
                    {
                        xtype: 'textfield',
                        flex: 1,
                        fieldLabel: 'Label',
                        name: 'keywords',
                        maxLength: 50
                    }
                ]
            }
        ];
        this.fbar = {
            xtype: 'toolbar',
            autoWidth: true,
            items: [
                {
                    xtype: 'button',
                    text: 'Save',
                    ref: '../updatebutton'
                },
                {
                    xtype: 'button',
                    text: 'Save As New',
                    hidden: true,
                    width: 75,
                    ref: '../createbutton'
                },
                {
                    xtype: 'spacer',
                    width: 50
                }
            ]
        };
        CandidateExperienceEditFormUi.superclass.initComponent.call(this);
    }
});