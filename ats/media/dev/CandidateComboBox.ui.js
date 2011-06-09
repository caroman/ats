/*
 * File: CandidateComboBox.ui.js
 * Date: Thu Jun 09 2011 08:24:48 GMT-0400 (EDT)
 * 
 * This file was generated by Ext Designer version xds-1.0.2.14.
 * http://www.extjs.com/products/designer/
 *
 * This file will be auto-generated each and everytime you export.
 *
 * Do NOT hand edit this file.
 */

CandidateComboBoxUi = Ext.extend(Ext.form.ComboBox, {
    store: 'CandidateComboBoxStore',
    valueField: 'id',
    displayField: 'id',
    forceSelection: true,
    hiddenName: 'candidate',
    pageSize: 25,
    submitValue: true,
    triggerAction: 'all',
    initComponent: function() {
        this.tpl = [
            '<tpl for="."><div class="x-combo-list-item">',
            '<b>ID:{id}</b>',
            ' {first_name}',
            ' {last_name}',
            '</div></tpl>'
        ];
        this.initialConfig = Ext.apply({
            minChars: 0
        }, this.initialConfig);
        CandidateComboBoxUi.superclass.initComponent.call(this);
    }
});
