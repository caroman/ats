/*
 * File: ActivityStore.js
 * Date: Thu Jun 09 2011 08:24:48 GMT-0400 (EDT)
 * 
 * This file was generated by Ext Designer version xds-1.0.2.14.
 * http://www.extjs.com/products/designer/
 *
 * This file will be auto-generated each and everytime you export.
 *
 * Do NOT hand edit this file.
 */

ActivityStore = Ext.extend(Ext.data.JsonStore, {
    constructor: function(cfg) {
        cfg = cfg || {};
        ActivityStore.superclass.constructor.call(this, Ext.apply({
            storeId: 'ActivityStore',
            url: '/ats/static/activity/list/',
            root: 'results',
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
Ext.reg('activitystore', ActivityStore);new ActivityStore();