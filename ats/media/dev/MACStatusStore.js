/*
 * File: MACStatusStore.js
 * Date: Sun Jun 05 2011 10:23:52 GMT-0400 (EDT)
 * 
 * This file was generated by Ext Designer version xds-1.0.2.14.
 * http://www.extjs.com/products/designer/
 *
 * This file will be auto-generated each and everytime you export.
 *
 * Do NOT hand edit this file.
 */

MACStatusStore = Ext.extend(Ext.data.JsonStore, {
    constructor: function(cfg) {
        cfg = cfg || {};
        MACStatusStore.superclass.constructor.call(this, Ext.apply({
            storeId: 'MACStatusStore',
            url: '/ats/static/mac/status/list/',
            root: 'results',
            restful: true,
            autoSave: false,
            fields: [
                {
                    name: 'id',
                    type: 'int',
                    mapping: 'pk'
                },
                {
                    name: 'title',
                    mapping: 'fields["title"]',
                    type: 'string'
                }
            ]
        }, cfg));
    }
});
Ext.reg('macstatusstore', MACStatusStore);new MACStatusStore();