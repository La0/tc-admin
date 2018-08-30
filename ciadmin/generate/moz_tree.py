# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file, You can
# obtain one at http://mozilla.org/MPL/2.0/.

from ..resources import Role


async def update_resources(resources):
    '''
    Manage the moz-tree:. roles.  These will soon go away, but need to be
    considered here for the moment to allow proper analysis of roles.
    '''
    resources.manage('Role=moz-tree:*')
    resources.add(Role(
        roleId='moz-tree:level:1',
        description='Deprecated',
        scopes=[
            'assume:moz-tree:level:1:gecko',
        ]))

    resources.add(Role(
        roleId='moz-tree:level:1:*',
        description='Deprecated',
        scopes=[
            'docker-worker:cache:level-1-*',
            'docker-worker:cache:tooltool-cache',
            'docker-worker:capability:device:loopbackAudio',
            'docker-worker:capability:device:loopbackVideo',
            'docker-worker:capability:privileged',
            'docker-worker:feature:allowPtrace',
            'docker-worker:image:quay.io/mozilla/builder:*',
            'docker-worker:image:quay.io/mozilla/decision:*',
            'docker-worker:image:taskcluster/builder:*',
            'docker-worker:image:taskcluster/tester:*',
            'docker-worker:image:taskclusterprivate/upload_symbols:*',
            'docker-worker:relengapi-proxy:tooltool.download.internal',
            'docker-worker:relengapi-proxy:tooltool.download.public',
            'generic-worker:cache:level-1-*',
            'generic-worker:os-group:aws-provisioner-v1/gecko-t-win10-64/Administrators',
            'generic-worker:os-group:aws-provisioner-v1/gecko-t-win7-32/Administrators',
            'generic-worker:run-as-administrator:aws-provisioner-v1/gecko-t-win10-64',
            'index:insert-task:docker.images.v2.level-1.*',
            'index:insert-task:garbage.*',
            'index:insert-task:gecko.cache.level-1.*',
            'notify:email:*',
            'project:releng:balrog:channel:*',
            'project:releng:balrog:server:dep',
            'project:releng:beetmover:action:*',
            'project:releng:beetmover:bucket:dep',
            'project:releng:beetmover:bucket:maven-staging',
            'project:releng:googleplay:dep',
            'project:releng:ship-it:staging',
            'project:releng:signing:cert:dep-signing',
            'project:releng:signing:format:*',
            'purge-cache:aws-provisioner-v1/*',
            'queue:cancel-task:gecko-level-1/*',
            'queue:create-task:aws-provisioner-v1/ami-test*',
            'queue:create-task:aws-provisioner-v1/android-api-*',
            'queue:create-task:aws-provisioner-v1/b2gbuild*',
            'queue:create-task:aws-provisioner-v1/b2gtest*',
            'queue:create-task:aws-provisioner-v1/balrog',
            'queue:create-task:aws-provisioner-v1/dbg-*',
            'queue:create-task:aws-provisioner-v1/desktop-test*',
            'queue:create-task:aws-provisioner-v1/flame-kk*',
            'queue:create-task:aws-provisioner-v1/gecko-1-*',
            'queue:create-task:aws-provisioner-v1/gecko-decision',
            'queue:create-task:aws-provisioner-v1/gecko-images',
            'queue:create-task:aws-provisioner-v1/gecko-misc',
            'queue:create-task:aws-provisioner-v1/gecko-symbol-upload',
            'queue:create-task:aws-provisioner-v1/gecko-t-*',
            'queue:create-task:aws-provisioner-v1/loan-1-*',
            'queue:create-task:aws-provisioner-v1/loan-t-*',
            'queue:create-task:aws-provisioner-v1/mulet-debug',
            'queue:create-task:aws-provisioner-v1/mulet-opt',
            'queue:create-task:aws-provisioner-v1/opt-*',
            'queue:create-task:aws-provisioner-v1/rustbuild',
            'queue:create-task:aws-provisioner-v1/spidermonkey',
            'queue:create-task:aws-provisioner-v1/symbol-upload',
            'queue:create-task:aws-provisioner-v1/taskcluster-images',
            'queue:create-task:buildbot-bridge/buildbot-bridge',
            'queue:create-task:dummy-test-provisioner/dummy-test-type',
            'queue:create-task:gecko-t-tc-worker/*',
            'queue:create-task:localprovisioner/*',
            'queue:create-task:low:scriptworker-prov-v1/balrog-dev',
            'queue:create-task:low:scriptworker-prov-v1/beetmoverworker-dev',
            'queue:create-task:medium:proj-autophone/*',
            'queue:create-task:medium:proj-awfy/*',
            'queue:create-task:null-provisioner/buildbot',
            'queue:create-task:null-provisioner/buildbot-try',
            'queue:create-task:packetnet/*',
            'queue:create-task:releng-hardware/*',
            'queue:create-task:scl3-puppet/os-x-10-10-gw',
            'queue:create-task:scl3-puppet/os-x-build-gw',
            'queue:create-task:tc-worker-provisioner/*',
            'queue:create-task:test-dummy-provisioner/*',
            'queue:create-task:low:aws-provisioner-v1/ami-test*',
            'queue:create-task:low:aws-provisioner-v1/android-api-*',
            'queue:create-task:low:aws-provisioner-v1/b2gbuild*',
            'queue:create-task:low:aws-provisioner-v1/b2gtest*',
            'queue:create-task:low:aws-provisioner-v1/balrog',
            'queue:create-task:low:aws-provisioner-v1/dbg-*',
            'queue:create-task:low:aws-provisioner-v1/desktop-test*',
            'queue:create-task:low:aws-provisioner-v1/flame-kk*',
            'queue:create-task:low:aws-provisioner-v1/gecko-1-*',
            'queue:create-task:low:aws-provisioner-v1/gecko-decision',
            'queue:create-task:low:aws-provisioner-v1/gecko-images',
            'queue:create-task:low:aws-provisioner-v1/gecko-misc',
            'queue:create-task:low:aws-provisioner-v1/gecko-symbol-upload',
            'queue:create-task:low:aws-provisioner-v1/gecko-t-*',
            'queue:create-task:low:aws-provisioner-v1/loan-1-*',
            'queue:create-task:low:aws-provisioner-v1/loan-t-*',
            'queue:create-task:low:aws-provisioner-v1/mulet-debug',
            'queue:create-task:low:aws-provisioner-v1/mulet-opt',
            'queue:create-task:low:aws-provisioner-v1/opt-*',
            'queue:create-task:low:aws-provisioner-v1/rustbuild',
            'queue:create-task:low:aws-provisioner-v1/spidermonkey',
            'queue:create-task:low:aws-provisioner-v1/symbol-upload',
            'queue:create-task:low:aws-provisioner-v1/taskcluster-images',
            'queue:create-task:low:buildbot-bridge/buildbot-bridge',
            'queue:create-task:low:dummy-test-provisioner/dummy-test-type',
            'queue:create-task:low:gecko-t-tc-worker/*',
            'queue:create-task:low:localprovisioner/*',
            'queue:create-task:low:manual-packet/tc-worker-qemu-v1',
            'queue:create-task:low:null-provisioner/buildbot',
            'queue:create-task:low:null-provisioner/buildbot-try',
            'queue:create-task:low:packetnet/*',
            'queue:create-task:low:releng-hardware/gecko-t-*',
            'queue:create-task:low:releng-hardware/my-talos',
            'queue:create-task:low:scl3-puppet/os-x-10-10-gw',
            'queue:create-task:low:scl3-puppet/os-x-build-gw',
            'queue:create-task:low:scriptworker-prov-v1/dep-pushapk',
            'queue:create-task:low:scriptworker-prov-v1/depsigning',
            'queue:create-task:low:scriptworker-prov-v1/shipit-dev',
            'queue:create-task:low:tc-worker-provisioner/*',
            'queue:create-task:low:test-dummy-provisioner/*',
            'queue:define-task:aws-provisioner-v1/build-c4-2xlarge',
            'queue:define-task:aws-provisioner-v1/taskcluster-images',
            'queue:define-task:aws-provisioner-v1/test-c4-2xlarge',
            'queue:define-task:dummy-test-provisioner/dummy-test-type',
            'queue:get-artifact:private/interactive/*',
            'queue:get-artifact:project/gecko/android-*',
            'queue:rerun-task:gecko-level-1/*',
            'queue:route:index.docker.images.v2.level-1.*',
            'queue:route:index.garbage.*',
            'queue:route:index.gecko.cache.level-1.*',
            'queue:route:project.releng.funsize.level-1.*',
            'queue:scheduler-id:gecko-level-1',
            'queue:route:notify.*',
            'scheduler:create-task-graph',
            'scheduler:extend-task-graph:*',
            'secrets:get:project/releng/gecko/build/level-1/*',
            'secrets:get:project/taskcluster/gecko/hgfingerprint',
            'worker:privileged:manual-packet/tc-worker-docker-v0',
            'queue:create-task:low:manual-packet/tc-worker-docker-v0',
            'worker:privileged:terraform-packet/tc-worker-docker-v1',
            'queue:create-task:low:terraform-packet/tc-worker-docker-v1',
            'worker:privileged:terraform-packet/tc-worker-docker-v1-*',
            'queue:create-task:low:terraform-packet/tc-worker-docker-v1-*',
            'worker:cache:level-1-*',
            'queue:create-task:medium:terraform-packet/tc-worker-docker-v1-*',
            'worker:relengapi-proxy:tooltool.download.internal',
            'worker:relengapi-proxy:tooltool.download.public',
        ]))

    resources.add(Role(
        roleId='moz-tree:level:1:gecko',
        description='Deprecated',
        scopes=[
            'assume:project:taskcluster:gecko:level-1-sccache-buckets',
            'assume:project:taskcluster:level-1-sccache-buckets',
            'generic-worker:allow-rdp:aws-provisioner-v1/gecko-1-b-win*',
            'generic-worker:allow-rdp:aws-provisioner-v1/gecko-t-win*',
            'project:releng:addons.mozilla.org:server:staging',
            'project:releng:balrog:action:*',
            'project:releng:beetmover:bucket:dep-partner',
            'project:releng:bouncer:action:submission',
            'project:releng:bouncer:server:staging',
            'project:releng:snapcraft:firefox:mock',
            'project:releng:treescript:action:*',
            'project:releng:treescript:action:tagging',
            'queue:create-task:low:aws-provisioner-v1/fp-gecko-*',
            'queue:create-task:low:manual-packet/tc-worker-docker-v1',
            'queue:create-task:low:scriptworker-prov-v1/addon-dev',
            'queue:create-task:low:scriptworker-prov-v1/balrog-dev',
            'queue:create-task:low:scriptworker-prov-v1/bouncer-dev',
            'queue:create-task:low:scriptworker-prov-v1/dep-pushsnap',
            'queue:create-task:low:scriptworker-prov-v1/signing-linux-dev',
            'queue:create-task:low:scriptworker-prov-v1/treescript-dev',
            'queue:create-task:low:scriptworker-prov-v1/treescript-v1',
            'queue:create-task:low:terraform-packet/*',
            'queue:get-artifact:releng/partner/*',
        ]))

    resources.add(Role(
        roleId='moz-tree:level:1:comm',
        description='Deprecated',
        scopes=[
            'assume:project:taskcluster:comm:level-1-sccache-buckets',
            'project:comm:thunderbird:releng:balrog:action:*',
            'project:comm:thunderbird:releng:balrog:server:dep',
            'project:comm:thunderbird:releng:beetmover:action:*',
            'project:comm:thunderbird:releng:beetmover:bucket:dep',
            'project:comm:thunderbird:releng:bouncer:action:*',
            'project:comm:thunderbird:releng:bouncer:server:staging',
            'project:comm:thunderbird:releng:ship-it:staging',
            'project:comm:thunderbird:releng:signing:cert:dep-signing',
            'project:comm:thunderbird:releng:signing:format:*',
            'project:comm:thunderbird:releng:treescript:action:push',
            'project:comm:thunderbird:releng:treescript:action:tagging',
            'project:comm:thunderbird:releng:treescript:action:version_bump',
            'queue:create-task:low:scriptworker-prov-v1/tb-balrog-dev',
            'queue:create-task:low:scriptworker-prov-v1/tb-beetmover-dev',
            'queue:create-task:low:scriptworker-prov-v1/tb-bouncer-dev',
            'queue:create-task:low:scriptworker-prov-v1/tb-depsigning',
            'queue:create-task:low:scriptworker-prov-v1/tb-shipit-dev',
            'queue:create-task:low:scriptworker-prov-v1/tb-treescript-comm-dev',
            'secrets:get:project/comm/thunderbird/releng/build/level-1/*',
        ]))

    resources.add(Role(
        roleId='moz-tree:level:2',
        description='Deprecated',
        scopes=[
            'assume:moz-tree:level:2:gecko',
        ]))

    resources.add(Role(
        roleId='moz-tree:level:2:*',
        description='Deprecated',
        scopes=[
            'docker-worker:cache:level-2-*',
            'docker-worker:capability:device:phone',
            'docker-worker:image:taskclusterprivate/phone-builder:*',
            'docker-worker:image:taskclusterprivate/tester-device:*',
            'generic-worker:cache:level-2-*',
            'generic-worker:os-group:aws-provisioner-v1/gecko-t-win7-32/Administrators',
            'generic-worker:os-group:aws-provisioner-v1/gecko-t-win10-64/Administrators',
            'generic-worker:run-as-administrator:aws-provisioner-v1/gecko-t-win10-64',
            'index:insert-task:docker.images.v2.level-2.*',
            'index:insert-task:gecko.cache.level-2.*',
            'queue:cancel-task:gecko-level-2/*',
            'queue:create-task:aws-provisioner-v1/ami-test*',
            'queue:create-task:aws-provisioner-v1/android-api-*',
            'queue:create-task:aws-provisioner-v1/b2gbuild*',
            'queue:create-task:aws-provisioner-v1/b2gtest*',
            'queue:create-task:aws-provisioner-v1/balrog',
            'queue:create-task:aws-provisioner-v1/dbg-*',
            'queue:create-task:aws-provisioner-v1/desktop-test*',
            'queue:create-task:aws-provisioner-v1/flame-kk*',
            'queue:create-task:aws-provisioner-v1/gecko-1-*',
            'queue:create-task:aws-provisioner-v1/gecko-2-*',
            'queue:create-task:aws-provisioner-v1/gecko-decision',
            'queue:create-task:aws-provisioner-v1/gecko-images',
            'queue:create-task:aws-provisioner-v1/gecko-misc',
            'queue:create-task:aws-provisioner-v1/gecko-symbol-upload',
            'queue:create-task:aws-provisioner-v1/gecko-t-*',
            'queue:create-task:aws-provisioner-v1/loan-1-*',
            'queue:create-task:aws-provisioner-v1/loan-t-*',
            'queue:create-task:aws-provisioner-v1/mulet-debug',
            'queue:create-task:aws-provisioner-v1/mulet-opt',
            'queue:create-task:aws-provisioner-v1/opt-*',
            'queue:create-task:aws-provisioner-v1/rustbuild',
            'queue:create-task:aws-provisioner-v1/spidermonkey',
            'queue:create-task:aws-provisioner-v1/symbol-upload',
            'queue:create-task:aws-provisioner-v1/taskcluster-images',
            'queue:create-task:aws-provisioner-v1/testdroid-device',
            'queue:create-task:buildbot-bridge/buildbot-bridge',
            'queue:create-task:dummy-test-provisioner/dummy-test-type',
            'queue:create-task:gecko-t-tc-worker/*',
            'queue:create-task:localprovisioner/*',
            'queue:create-task:null-provisioner/buildbot',
            'queue:create-task:null-provisioner/buildbot-try',
            'queue:create-task:packetnet/*',
            'queue:create-task:releng-hardware/gecko-t-*',
            'queue:create-task:scl3-puppet/os-x-10-10-gw',
            'queue:create-task:scl3-puppet/os-x-build-gw',
            'queue:create-task:tc-worker-provisioner/*',
            'queue:create-task:test-dummy-provisioner/*',
            'queue:create-task:very-low:aws-provisioner-v1/ami-test*',
            'queue:create-task:very-low:aws-provisioner-v1/android-api-*',
            'queue:create-task:very-low:aws-provisioner-v1/b2gbuild*',
            'queue:create-task:very-low:aws-provisioner-v1/b2gtest*',
            'queue:create-task:very-low:aws-provisioner-v1/balrog',
            'queue:create-task:very-low:aws-provisioner-v1/dbg-*',
            'queue:create-task:very-low:aws-provisioner-v1/desktop-test*',
            'queue:create-task:very-low:aws-provisioner-v1/flame-kk*',
            'queue:create-task:very-low:aws-provisioner-v1/gecko-1-*',
            'queue:create-task:very-low:aws-provisioner-v1/gecko-2-*',
            'queue:create-task:very-low:aws-provisioner-v1/gecko-decision',
            'queue:create-task:very-low:aws-provisioner-v1/gecko-images',
            'queue:create-task:very-low:aws-provisioner-v1/gecko-misc',
            'queue:create-task:very-low:aws-provisioner-v1/gecko-symbol-upload',
            'queue:create-task:very-low:aws-provisioner-v1/gecko-t-*',
            'queue:create-task:very-low:aws-provisioner-v1/loan-1-*',
            'queue:create-task:very-low:aws-provisioner-v1/loan-t-*',
            'queue:create-task:very-low:aws-provisioner-v1/mulet-debug',
            'queue:create-task:very-low:aws-provisioner-v1/mulet-opt',
            'queue:create-task:very-low:aws-provisioner-v1/opt-*',
            'queue:create-task:very-low:aws-provisioner-v1/rustbuild',
            'queue:create-task:very-low:aws-provisioner-v1/spidermonkey',
            'queue:create-task:very-low:aws-provisioner-v1/symbol-upload',
            'queue:create-task:very-low:aws-provisioner-v1/taskcluster-images',
            'queue:create-task:very-low:aws-provisioner-v1/testdroid-device',
            'queue:create-task:very-low:buildbot-bridge/buildbot-bridge',
            'queue:create-task:very-low:dummy-test-provisioner/dummy-test-type',
            'queue:create-task:very-low:gecko-t-tc-worker/*',
            'queue:create-task:very-low:localprovisioner/*',
            'queue:create-task:very-low:null-provisioner/buildbot',
            'queue:create-task:very-low:null-provisioner/buildbot-try',
            'queue:create-task:very-low:packetnet/*',
            'queue:create-task:very-low:releng-hardware/gecko-t-*',
            'queue:create-task:very-low:scl3-puppet/os-x-10-10-gw',
            'queue:create-task:very-low:scl3-puppet/os-x-build-gw',
            'queue:create-task:very-low:tc-worker-provisioner/*',
            'queue:create-task:very-low:test-dummy-provisioner/*',
            'queue:route:index.docker.images.v2.level-2.*',
            'queue:route:index.gecko.cache.level-2.*',
            'queue:scheduler-id:gecko-level-2',
            'secrets:get:project/releng/gecko/build/level-2/*',
            'secrets:get:project/taskcluster/gecko/build/level-2/*',
        ]))

    resources.add(Role(
        roleId='moz-tree:level:2:gecko',
        description='Deprecated',
        scopes=[
            'assume:moz-tree:level:1:gecko',
            'assume:project:taskcluster:gecko:level-2-sccache-buckets',
            'assume:project:taskcluster:level-2-sccache-buckets',
            'queue:rerun-task:gecko-level-2/*',
        ]))

    resources.add(Role(
        roleId='moz-tree:level:2:comm',
        description='Deprecated',
        scopes=[
            'assume:moz-tree:level:1:comm',
            'assume:project:taskcluster:comm:level-2-sccache-buckets',
        ]))

    resources.add(Role(
        roleId='moz-tree:level:3',
        description='Deprecated',
        scopes=[
            'assume:moz-tree:level:3:gecko',
        ]))

    resources.add(Role(
        roleId='moz-tree:level:3:*',
        description='Deprecated',
        scopes=[
            'auth:aws-s3:read-write:public-qemu-images/repository/hg.mozilla.org/mozilla-central/*',
            'docker-worker:cache:level-3-*',
            'docker-worker:feature:balrogStageVPNProxy',
            'docker-worker:feature:balrogVPNProxy',
            'docker-worker:image:taskclusterprivate/taskcluster-vpn-proxy:*',
            'generic-worker:cache:level-3-*',
            'generic-worker:os-group:aws-provisioner-v1/gecko-t-win7-32/Administrators',
            'generic-worker:os-group:aws-provisioner-v1/gecko-t-win10-64/Administrators',
            'generic-worker:run-as-administrator:aws-provisioner-v1/gecko-t-win10-64',
            'index:insert-task:docker.images.v2.level-3.*',
            'index:insert-task:gecko.cache.level-3.*',
            'project:releng:balrog:server:beta',
            'project:releng:balrog:server:release',
            'project:releng:balrog:server:esr',
            'project:releng:beetmover:bucket:release',
            'project:releng:ship-it:production',
            'project:releng:googleplay:beta',
            'queue:cancel-task:gecko-level-3/*',
            'queue:create-task:aws-provisioner-v1/ami-test*',
            'queue:create-task:aws-provisioner-v1/android-api-*',
            'queue:create-task:aws-provisioner-v1/b2gbuild*',
            'queue:create-task:aws-provisioner-v1/b2gtest*',
            'queue:create-task:aws-provisioner-v1/balrog',
            'queue:create-task:aws-provisioner-v1/dbg-*',
            'queue:create-task:aws-provisioner-v1/desktop-test*',
            'queue:create-task:aws-provisioner-v1/flame-kk*',
            'queue:create-task:aws-provisioner-v1/gecko-1-*',
            'queue:create-task:aws-provisioner-v1/gecko-2-*',
            'queue:create-task:aws-provisioner-v1/gecko-3-*',
            'queue:create-task:aws-provisioner-v1/gecko-decision',
            'queue:create-task:aws-provisioner-v1/gecko-images',
            'queue:create-task:aws-provisioner-v1/gecko-misc',
            'queue:create-task:aws-provisioner-v1/gecko-symbol-upload',
            'queue:create-task:aws-provisioner-v1/gecko-t-*',
            'queue:create-task:aws-provisioner-v1/loan-1-*',
            'queue:create-task:aws-provisioner-v1/loan-t-*',
            'queue:create-task:aws-provisioner-v1/mulet-debug',
            'queue:create-task:aws-provisioner-v1/mulet-opt',
            'queue:create-task:aws-provisioner-v1/opt-*',
            'queue:create-task:aws-provisioner-v1/rustbuild',
            'queue:create-task:aws-provisioner-v1/spidermonkey',
            'queue:create-task:aws-provisioner-v1/symbol-upload',
            'queue:create-task:aws-provisioner-v1/taskcluster-images',
            'queue:create-task:aws-provisioner-v1/testdroid-device',
            'queue:create-task:buildbot-bridge/buildbot-bridge',
            'queue:create-task:dummy-test-provisioner/dummy-test-type',
            'queue:create-task:gecko-t-tc-worker/*',
            'queue:create-task:highest:aws-provisioner-v1/ami-test*',
            'queue:create-task:highest:aws-provisioner-v1/android-api-*',
            'queue:create-task:highest:aws-provisioner-v1/b2gbuild*',
            'queue:create-task:highest:aws-provisioner-v1/b2gtest*',
            'queue:create-task:highest:aws-provisioner-v1/balrog',
            'queue:create-task:highest:aws-provisioner-v1/dbg-*',
            'queue:create-task:highest:aws-provisioner-v1/desktop-test*',
            'queue:create-task:highest:aws-provisioner-v1/flame-kk*',
            'queue:create-task:highest:aws-provisioner-v1/gecko-1-*',
            'queue:create-task:highest:aws-provisioner-v1/gecko-2-*',
            'queue:create-task:highest:aws-provisioner-v1/gecko-3-*',
            'queue:create-task:highest:aws-provisioner-v1/gecko-decision',
            'queue:create-task:highest:aws-provisioner-v1/gecko-images',
            'queue:create-task:highest:aws-provisioner-v1/gecko-misc',
            'queue:create-task:highest:aws-provisioner-v1/gecko-symbol-upload',
            'queue:create-task:highest:aws-provisioner-v1/gecko-t-*',
            'queue:create-task:highest:aws-provisioner-v1/loan-1-*',
            'queue:create-task:highest:aws-provisioner-v1/loan-t-*',
            'queue:create-task:highest:aws-provisioner-v1/mulet-debug',
            'queue:create-task:highest:aws-provisioner-v1/mulet-opt',
            'queue:create-task:highest:aws-provisioner-v1/opt-*',
            'queue:create-task:highest:aws-provisioner-v1/rustbuild',
            'queue:create-task:highest:aws-provisioner-v1/spidermonkey',
            'queue:create-task:highest:aws-provisioner-v1/symbol-upload',
            'queue:create-task:highest:aws-provisioner-v1/taskcluster-images',
            'queue:create-task:highest:aws-provisioner-v1/testdroid-device',
            'queue:create-task:highest:buildbot-bridge/buildbot-bridge',
            'queue:create-task:highest:dummy-test-provisioner/dummy-test-type',
            'queue:create-task:highest:gecko-t-tc-worker/*',
            'queue:create-task:highest:localprovisioner/*',
            'queue:create-task:highest:null-provisioner/buildbot',
            'queue:create-task:highest:null-provisioner/buildbot-try',
            'queue:create-task:highest:null-provisioner/human-breakpoint',
            'queue:create-task:highest:packetnet/*',
            'queue:create-task:highest:releng-hardware/gecko-t-*',
            'queue:create-task:highest:scl3-puppet/os-x-10-10-gw',
            'queue:create-task:highest:scl3-puppet/os-x-build-gw',
            'queue:create-task:highest:scriptworker-prov-v1/dep-pushapk',
            'queue:create-task:highest:scriptworker-prov-v1/pushapk-v1',
            'queue:create-task:highest:scriptworker-prov-v1/depsigning',
            'queue:create-task:highest:scriptworker-prov-v1/dummy-worker-transpar',
            'queue:create-task:highest:scriptworker-prov-v1/signing-linux-dev',
            'queue:create-task:highest:tc-worker-provisioner/*',
            'queue:create-task:highest:test-dummy-provisioner/*',
            'queue:create-task:localprovisioner/*',
            'queue:create-task:null-provisioner/buildbot',
            'queue:create-task:null-provisioner/buildbot-try',
            'queue:create-task:packetnet/*',
            'queue:create-task:releng-hardware/gecko-t-*',
            'queue:create-task:scl3-puppet/os-x-10-10-gw',
            'queue:create-task:scl3-puppet/os-x-build-gw',
            'queue:create-task:tc-worker-provisioner/*',
            'queue:create-task:test-dummy-provisioner/*',
            'queue:get-artifact:private/docker-worker/*',
            'queue:route:index.docker.images.v2.level-3.*',
            'queue:route:index.gecko.cache.level-3.*',
            'queue:scheduler-id:gecko-level-3',
            'secrets:get:project/releng/gecko/build/level-3/*',
            'secrets:get:project/releng/snapcraft/firefox/edge',
            'secrets:get:project/taskcluster/gecko/build/level-3/*',
        ]))

    resources.add(Role(
        roleId='moz-tree:level:3:gecko',
        description='Deprecated',
        scopes=[
            'assume:moz-tree:level:2:gecko',
            'assume:project:taskcluster:gecko:level-3-sccache-buckets',
            'assume:project:taskcluster:level-3-sccache-buckets',
            'auth:aws-s3:read-write:tc-gp-private-1d-us-east-1/releng/mbsdiff-cache/',
            'project:releng:addons.mozilla.org:server:production',
            'project:releng:beetmover:action:push-to-maven',
            'project:releng:beetmover:action:push-to-partner',
            'project:releng:beetmover:bucket:maven-production',
            'project:releng:beetmover:bucket:partner',
            'project:releng:bouncer:action:aliases',
            'project:releng:bouncer:action:locations',
            'project:releng:bouncer:action:submission',
            'project:releng:bouncer:server:production',
            'project:releng:bouncer:server:staging',
            'project:releng:googleplay:release',
            'project:releng:ship-it:action:mark-as-shipped',
            'project:releng:ship-it:action:mark-as-started',
            'project:releng:ship-it:action:submit-mar-manifest',
            'project:releng:ship-it:server:production',
            'project:releng:ship-it:server:staging',
            'project:releng:signing:cert:nightly-signing',
            'project:releng:signing:cert:release-signing',
            'project:releng:snapcraft:firefox:beta',
            'project:releng:snapcraft:firefox:candidate',
            'project:releng:snapcraft:firefox:esr',
            'queue:create-task:highest:aws-provisioner-v1/taskcluster-generic',
            'queue:create-task:highest:proj-autophone/*',
            'queue:create-task:highest:scriptworker-prov-v1/addon-v1',
            'queue:create-task:highest:scriptworker-prov-v1/balrogworker-v1',
            'queue:create-task:highest:scriptworker-prov-v1/beetmoverworker-v1',
            'queue:create-task:highest:scriptworker-prov-v1/bouncer-dev',
            'queue:create-task:highest:scriptworker-prov-v1/bouncer-v1',
            'queue:create-task:highest:scriptworker-prov-v1/pushsnap-v1',
            'queue:create-task:highest:scriptworker-prov-v1/shipit-v1',
            'queue:create-task:highest:scriptworker-prov-v1/signing-linux-v1',
            'queue:create-task:highest:scriptworker-prov-v1/treescript-v1',
            'queue:create-task:highest:terraform-packet/gecko-t-*',
            'queue:rerun-task:gecko-level-3/*',
            'queue:route:notify.email.release+tcstaging@mozilla.com.',
            'queue:route:notify.email.release-automation-notifications@mozilla.com.*',
            'queue:route:tc-treeherder.v2.*',
            'queue:route:index.gecko.heavyprofile.*',
            'secrets:get:project/releng/snapcraft/firefox/candidate',
        ]))

    resources.add(Role(
        roleId='moz-tree:level:3:comm',
        description='Deprecated',
        scopes=[
            'assume:moz-tree:level:2:comm',
            'assume:project:taskcluster:comm:level-3-sccache-buckets',
            'queue:create-task:highest:scriptworker-prov-v1/tb-balrog-dev',
            'queue:create-task:highest:scriptworker-prov-v1/tb-beetmover-dev',
            'queue:create-task:highest:scriptworker-prov-v1/tb-depsigning',
            'secrets:get:project/comm/thunderbird/releng/build/level-3/*',
        ]))

    resources.add(Role(
        roleId='moz-tree:nss',
        description='Deprecated',
        scopes=[
            'docker-worker:feature:allowPtrace',
            'queue:create-task:aws-provisioner-v1/hg-worker',
            'queue:create-task:aws-provisioner-v1/nss-win2012r2',
            'queue:create-task:localprovisioner/nss-aarch64',
            'queue:create-task:localprovisioner/nss-macos-10-12',
            'queue:create-task:localprovisioner/nss-rpi',
            'queue:route:index.docker.images.v1.nss.*',
            'queue:route:tc-treeherder-stage.nss.*',
            'queue:route:tc-treeherder-stage.v2.nss.*',
            'queue:route:tc-treeherder.nss.*',
            'queue:route:tc-treeherder.v2.nss.*',
            'scheduler:create-task-graph',
            'scheduler:extend-task-graph:*',
        ]))

    resources.add(Role(
        roleId='moz-tree:nss-try',
        description='Deprecated',
        scopes=[
            'docker-worker:feature:allowPtrace',
            'queue:create-task:aws-provisioner-v1/ami-test-win2012r2',
            'queue:create-task:aws-provisioner-v1/gecko-1-b-win*',
            'queue:create-task:aws-provisioner-v1/hg-worker',
            'queue:create-task:aws-provisioner-v1/nss-*',
            'queue:create-task:aws-provisioner-v1/win2012r2',
            'queue:create-task:localprovisioner/nss-aarch64',
            'queue:create-task:localprovisioner/nss-macos-10-12',
            'queue:route:index.docker.images.v1.nss-try.*',
            'queue:route:tc-treeherder-stage.nss-try.*',
            'queue:route:tc-treeherder-stage.v2.nss-try.*',
            'queue:route:tc-treeherder.nss-try.*',
            'queue:route:tc-treeherder.v2.nss-try.*',
            'scheduler:create-task-graph',
            'scheduler:extend-task-graph:*',
        ]))
