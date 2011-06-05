/*
 * File: MACStore.js
 * Date: Wed Jun 01 2011 08:49:10 GMT-0400 (EDT)
 * 
 * This file was generated by Ext Designer version xds-1.0.2.14.
 * http://www.extjs.com/products/designer/
 *
 * This file will be auto-generated each and everytime you export.
 *
 * Do NOT hand edit this file.
 */

MACStore = Ext.extend(Ext.data.JsonStore, {
    constructor: function(cfg) {
        cfg = cfg || {};
        MACStore.superclass.constructor.call(this, Ext.apply({
            storeId: 'MACStore',
            root: 'results',
            url: '/ats/main/mac/list/',
            restful: true,
            remoteSort: true,
            fields: [
                {
                    name: 'id',
                    mapping: 'pk',
                    type: 'int'
                },
                {
                    name: 'candidate',
                    mapping: 'fields["candidate"]'
                },
                {
                    name: 'mandate',
                    mapping: 'fields["mandate"]'
                },
                {
                    name: 'date',
                    mapping: 'fields["date"]',
                    type: 'date',
                    dateFormat: 'Y-m-d'
                },
                {
                    name: 'activity',
                    mapping: 'fields["activity"]'
                },
                {
                    name: 'status',
                    mapping: 'fields["status"]'
                },
                {
                    name: 'created_by',
                    mapping: 'fields["created_by"]'
                },
                {
                    name: 'description',
                    mapping: 'fields["description"]',
                    type: 'string'
                }
            ]
        }, cfg));
    }
});
Ext.reg('macstore', MACStore);new MACStore();