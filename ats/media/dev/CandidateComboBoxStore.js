/*
 * File: CandidateComboBoxStore.js
 * Date: Thu Jun 09 2011 08:24:48 GMT-0400 (EDT)
 * 
 * This file was generated by Ext Designer version xds-1.0.2.14.
 * http://www.extjs.com/products/designer/
 *
 * This file will be auto-generated each and everytime you export.
 *
 * Do NOT hand edit this file.
 */

CandidateComboBoxStore = Ext.extend(Ext.data.JsonStore, {
    constructor: function(cfg) {
        cfg = cfg || {};
        CandidateComboBoxStore.superclass.constructor.call(this, Ext.apply({
            storeId: 'CandidateComboBoxStore',
            url: '/ats/main/candidate/list/combobox/',
            root: 'results',
            restful: true,
            fields: [
                {
                    name: 'id',
                    type: 'int',
                    mapping: 'pk'
                },
                {
                    name: 'first_name',
                    type: 'string',
                    mapping: 'fields["first_name"]'
                },
                {
                    name: 'last_name',
                    type: 'string',
                    mapping: 'fields["last_name"]'
                }
            ]
        }, cfg));
    }
});
Ext.reg('candidatecomboboxstore', CandidateComboBoxStore);new CandidateComboBoxStore();