/*
 * File: MandateStore.js
 * Date: Sun Jun 05 2011 10:23:52 GMT-0400 (EDT)
 * 
 * This file was generated by Ext Designer version xds-1.0.2.14.
 * http://www.extjs.com/products/designer/
 *
 * This file will be auto-generated each and everytime you export.
 *
 * Do NOT hand edit this file.
 */

MandateStore = Ext.extend(Ext.data.JsonStore, {
    constructor: function(cfg) {
        cfg = cfg || {};
        MandateStore.superclass.constructor.call(this, Ext.apply({
            storeId: 'MandateStore',
            root: 'results',
            url: '/ats/main/mandate/list/',
            restful: true,
            remoteSort: true,
            fields: [
                {
                    name: 'id',
                    mapping: 'pk',
                    type: 'int'
                },
                {
                    name: 'title',
                    mapping: 'fields["title"]',
                    type: 'string'
                },
                {
                    name: 'posting_end_date',
                    mapping: 'fields["posting_end_date"]',
                    type: 'date',
                    dateFormat: 'Y-m-d'
                },
                {
                    name: 'posting_start_date',
                    mapping: 'fields["posting_start_date"]',
                    type: 'date',
                    dateFormat: 'Y-m-d'
                },
                {
                    name: 'created_by__username',
                    mapping: 'fields["created_by"]["fields"]["username"]',
                    type: 'string'
                },
                {
                    name: 'responsability',
                    mapping: 'fields["responsability"]'
                },
                {
                    name: 'requirement',
                    mapping: 'fields["requirement"]'
                },
                {
                    name: 'status',
                    mapping: 'fields["status"]'
                },
                {
                    name: 'hiring_manager',
                    mapping: 'fields["hiring_manager"]'
                },
                {
                    name: 'candidate_count',
                    mapping: 'extras["candidate_count"]',
                    type: 'int'
                },
                {
                    name: 'posting_number',
                    mapping: 'fields["posting_number"]',
                    type: 'string'
                },
                {
                    name: 'confidential',
                    mapping: 'fields["confidential"]',
                    type: 'boolean'
                },
                {
                    name: 'city',
                    mapping: 'fields["city"]',
                    type: 'string'
                },
                {
                    name: 'candidate_source',
                    mapping: 'fields["candidate_source"]',
                    type: 'string'
                },
                {
                    name: 'consulting_time',
                    mapping: 'fields["consulting_time"]',
                    type: 'float'
                },
                {
                    name: 'posting_sources',
                    mapping: 'fields["posting_sources"]',
                    type: 'string'
                },
                {
                    name: 'comments',
                    mapping: 'fields["comments"]',
                    type: 'string'
                },
                {
                    name: 'start_date',
                    mapping: 'fields["start_date"]',
                    type: 'date',
                    dateFormat: 'Y-m-d'
                },
                {
                    name: 'end_date',
                    mapping: 'fields["end_date"]',
                    type: 'date',
                    dateFormat: 'Y-m-d'
                },
                {
                    name: 'hired_number',
                    mapping: 'fields["hired_number"]',
                    type: 'int'
                }
            ]
        }, cfg));
    }
});
Ext.reg('mandatestore', MandateStore);new MandateStore();