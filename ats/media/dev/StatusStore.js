/*
 * File: StatusStore.js
 * Date: Mon Mar 28 2011 22:47:35 GMT-0400 (EDT)
 * 
 * This file was generated by Ext Designer version xds-1.0.2.14.
 * http://www.extjs.com/products/designer/
 *
 * This file will be auto-generated each and everytime you export.
 *
 * Do NOT hand edit this file.
 */

StatusStore = Ext.extend(Ext.data.JsonStore, {
    constructor: function(cfg) {
        cfg = cfg || {};
        StatusStore.superclass.constructor.call(this, Ext.apply({
            storeId: 'StatusStore',
            url: '/ats/static/status/list/',
            root: 'results',
            autoLoad: true,
            restful: true,
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
Ext.reg('statusstore', StatusStore);new StatusStore();