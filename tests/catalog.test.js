'use strict';

/**
 * Tests for catalog.json file
 */

const _ = require('lodash');
const fs = require('fs');

const catalog = JSON.parse(fs.readFileSync('catalog.json'));
const requiredFieldsTemplate = JSON.parse(fs.readFileSync('required_fields_project_template.json'));

test('Catalog entries have all required fields', () => {
    _.each(catalog, (entry, index) => {
        _.forOwn(requiredFieldsTemplate, (value, propertyName) => {
            if (propertyName === 'Labor_Hours' && index < 364) {
                // Old projects didn't require Labor_Hours, so don't enforce this check for them.
                return
            }
            expect(entry).toHaveProperty(propertyName);
        });
    });
});