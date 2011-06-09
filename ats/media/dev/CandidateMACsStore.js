/*
 * File: CandidateMACsStore.js
 * Date: Thu Jun 09 2011 08:24:48 GMT-0400 (EDT)
 * 
 * This file was generated by Ext Designer version xds-1.0.2.14.
 * http://www.extjs.com/products/designer/
 *
 * This file will be auto-generated each and everytime you export.
 *
 * Do NOT hand edit this file.
 */

CandidateMACsStore = Ext.extend(Ext.data.JsonStore, {
    constructor: function(cfg) {
        cfg = cfg || {};
        CandidateMACsStore.superclass.constructor.call(this, Ext.apply({
            storeId: 'CandidateMACsStore',
            url: '/ats/main/mac/list/',
            root: 'results',
            restful: true,
            remoteSort: true,
            fields: [
                {
                    name: 'mandate',
                    mapping: 'fields["mandate"]'
                },
                {
                    name: 'activity',
                    mapping: 'fields["activity"]'
                },
                {
                    name: 'status',
                    mapping: 'fields["status"]',
                    defaultValue: ''
                },
                {
                    name: 'date',
                    mapping: 'fields["date"]',
                    type: 'date'
                },
                {
                    name: 'description',
                    mapping: 'fields["description"]',
                    type: 'string'
                },
                {
                    name: 'id',
                    mapping: 'pk',
                    type: 'int'
                }
            ]
        }, cfg));
    }
});
Ext.reg('candidatemacsstore', CandidateMACsStore);new CandidateMACsStore();