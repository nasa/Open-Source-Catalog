'use strict';

/**
 * Tests for catalog.json file
 */

const _ = require('lodash');
const fs = require('fs');
const assert = require('assert');

const catalog = JSON.parse(fs.readFileSync('catalog.json'));
const requiredFieldsTemplate = JSON.parse(fs.readFileSync('required_fields_project_template.json'));

const maxIndexWithoutLaborHours = 364;

test('Catalog entries have all required fields', () => {
    _.each(catalog, (entry, index) => {
        _.forOwn(requiredFieldsTemplate, (value, propertyName) => {
            if (propertyName === 'Labor_Hours' && index < maxIndexWithoutLaborHours) {
                // Old projects didn't require Labor_Hours, so don't enforce this check for them.
                return;
            }
            expect(entry).toHaveProperty(propertyName);
        });
    });
});

test('Catalog entries have correct types', () => {
    _.each(catalog, (entry) => {
        _.forOwn(requiredFieldsTemplate, (templateEntry, propertyName) => {
            if (_.has(entry, propertyName)) {
                const expectedType = typeof templateEntry;
                const entryType = typeof entry[propertyName];
                const name = entry['Software'];
                assert.strictEqual(entryType, expectedType,
                    'Expected "' +
                    propertyName +
                    '" attribute to have type \'' +
                    expectedType + '\' but it had type \'' +
                    entryType +
                    '\' for software package: ' +
                    name);
            }
        });
    });
});