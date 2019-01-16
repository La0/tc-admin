# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file, You can
# obtain one at http://mozilla.org/MPL/2.0/.

import functools

MODIFIERS = {}


def modifier(fn):
    MODIFIERS[fn.__name__] = fn
    return fn


@modifier
def remove_hook_schedules(resources):
    '''
    Remove schedules from all managed hooks, so that they do not run and create tasks.
    '''
    def modify(resource):
        if resource.kind != 'Hook':
            return resource
        if not resource.schedule:
            return resource
        return resource.evolve(schedule=[])
    return resources.map(modify)


async def modify_resources(resources, environment):
    '''
    Apply any `modify_resources` functions to the given resources, and return
    a new set of resources.
    '''
    for mod in environment.modify_resources:
        if mod not in MODIFIERS:
            raise KeyError('No modify_resources function named {}'.format(mod))
        resources = MODIFIERS[mod](resources)
    return resources