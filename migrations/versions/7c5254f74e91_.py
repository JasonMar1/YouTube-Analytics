"""empty message

Revision ID: 7c5254f74e91
Revises: 972f497bf6a2
Create Date: 2024-08-23 19:19:21.657401

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '7c5254f74e91'
down_revision = '972f497bf6a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('deviceType',
    sa.Column('deviceType', sa.String(length=50), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('views', sa.Integer(), nullable=True),
    sa.Column('adImpressions', sa.Integer(), nullable=True),
    sa.Column('annotationClickableImpressions', sa.Integer(), nullable=True),
    sa.Column('annotationClicks', sa.Integer(), nullable=True),
    sa.Column('annotationClickThroughRate', sa.Float(), nullable=True),
    sa.Column('annotationClosableImpressions', sa.Integer(), nullable=True),
    sa.Column('annotationCloses', sa.Integer(), nullable=True),
    sa.Column('annotationCloseRate', sa.Float(), nullable=True),
    sa.Column('annotationImpressions', sa.Integer(), nullable=True),
    sa.Column('audienceWatchRatio', sa.Float(), nullable=True),
    sa.Column('averageViewDuration', sa.Float(), nullable=True),
    sa.Column('averageViewPercentage', sa.Float(), nullable=True),
    sa.Column('cardClickRate', sa.Float(), nullable=True),
    sa.Column('cardClicks', sa.Integer(), nullable=True),
    sa.Column('cardImpressions', sa.Integer(), nullable=True),
    sa.Column('cardTeaserClickRate', sa.Float(), nullable=True),
    sa.Column('cardTeaserClicks', sa.Integer(), nullable=True),
    sa.Column('cardTeaserImpressions', sa.Integer(), nullable=True),
    sa.Column('comments', sa.Integer(), nullable=True),
    sa.Column('cpm', sa.Float(), nullable=True),
    sa.Column('dislikes', sa.Integer(), nullable=True),
    sa.Column('estimatedMinutesWatched', sa.Integer(), nullable=True),
    sa.Column('likes', sa.Integer(), nullable=True),
    sa.Column('playbackBasedCpm', sa.Float(), nullable=True),
    sa.Column('playlistStarts', sa.Integer(), nullable=True),
    sa.Column('savesAdded', sa.Integer(), nullable=True),
    sa.Column('savesRemoved', sa.Integer(), nullable=True),
    sa.Column('shares', sa.Integer(), nullable=True),
    sa.Column('subscribersGained', sa.Integer(), nullable=True),
    sa.Column('subscribersLost', sa.Integer(), nullable=True),
    sa.Column('videosAddedToPlaylists', sa.Integer(), nullable=True),
    sa.Column('videosRemovedFromPlaylists', sa.Integer(), nullable=True),
    sa.Column('viewerPercentage', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('gender',
    sa.Column('gender', sa.String(length=10), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('views', sa.Integer(), nullable=True),
    sa.Column('adImpressions', sa.Integer(), nullable=True),
    sa.Column('annotationClickableImpressions', sa.Integer(), nullable=True),
    sa.Column('annotationClicks', sa.Integer(), nullable=True),
    sa.Column('annotationClickThroughRate', sa.Float(), nullable=True),
    sa.Column('annotationClosableImpressions', sa.Integer(), nullable=True),
    sa.Column('annotationCloses', sa.Integer(), nullable=True),
    sa.Column('annotationCloseRate', sa.Float(), nullable=True),
    sa.Column('annotationImpressions', sa.Integer(), nullable=True),
    sa.Column('audienceWatchRatio', sa.Float(), nullable=True),
    sa.Column('averageViewDuration', sa.Float(), nullable=True),
    sa.Column('averageViewPercentage', sa.Float(), nullable=True),
    sa.Column('cardClickRate', sa.Float(), nullable=True),
    sa.Column('cardClicks', sa.Integer(), nullable=True),
    sa.Column('cardImpressions', sa.Integer(), nullable=True),
    sa.Column('cardTeaserClickRate', sa.Float(), nullable=True),
    sa.Column('cardTeaserClicks', sa.Integer(), nullable=True),
    sa.Column('cardTeaserImpressions', sa.Integer(), nullable=True),
    sa.Column('comments', sa.Integer(), nullable=True),
    sa.Column('cpm', sa.Float(), nullable=True),
    sa.Column('dislikes', sa.Integer(), nullable=True),
    sa.Column('estimatedMinutesWatched', sa.Integer(), nullable=True),
    sa.Column('likes', sa.Integer(), nullable=True),
    sa.Column('playbackBasedCpm', sa.Float(), nullable=True),
    sa.Column('playlistStarts', sa.Integer(), nullable=True),
    sa.Column('savesAdded', sa.Integer(), nullable=True),
    sa.Column('savesRemoved', sa.Integer(), nullable=True),
    sa.Column('shares', sa.Integer(), nullable=True),
    sa.Column('subscribersGained', sa.Integer(), nullable=True),
    sa.Column('subscribersLost', sa.Integer(), nullable=True),
    sa.Column('videosAddedToPlaylists', sa.Integer(), nullable=True),
    sa.Column('videosRemovedFromPlaylists', sa.Integer(), nullable=True),
    sa.Column('viewerPercentage', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sharing_service',
    sa.Column('sharingService', sa.String(length=50), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('views', sa.Integer(), nullable=True),
    sa.Column('adImpressions', sa.Integer(), nullable=True),
    sa.Column('annotationClickableImpressions', sa.Integer(), nullable=True),
    sa.Column('annotationClicks', sa.Integer(), nullable=True),
    sa.Column('annotationClickThroughRate', sa.Float(), nullable=True),
    sa.Column('annotationClosableImpressions', sa.Integer(), nullable=True),
    sa.Column('annotationCloses', sa.Integer(), nullable=True),
    sa.Column('annotationCloseRate', sa.Float(), nullable=True),
    sa.Column('annotationImpressions', sa.Integer(), nullable=True),
    sa.Column('audienceWatchRatio', sa.Float(), nullable=True),
    sa.Column('averageViewDuration', sa.Float(), nullable=True),
    sa.Column('averageViewPercentage', sa.Float(), nullable=True),
    sa.Column('cardClickRate', sa.Float(), nullable=True),
    sa.Column('cardClicks', sa.Integer(), nullable=True),
    sa.Column('cardImpressions', sa.Integer(), nullable=True),
    sa.Column('cardTeaserClickRate', sa.Float(), nullable=True),
    sa.Column('cardTeaserClicks', sa.Integer(), nullable=True),
    sa.Column('cardTeaserImpressions', sa.Integer(), nullable=True),
    sa.Column('comments', sa.Integer(), nullable=True),
    sa.Column('cpm', sa.Float(), nullable=True),
    sa.Column('dislikes', sa.Integer(), nullable=True),
    sa.Column('estimatedMinutesWatched', sa.Integer(), nullable=True),
    sa.Column('likes', sa.Integer(), nullable=True),
    sa.Column('playbackBasedCpm', sa.Float(), nullable=True),
    sa.Column('playlistStarts', sa.Integer(), nullable=True),
    sa.Column('savesAdded', sa.Integer(), nullable=True),
    sa.Column('savesRemoved', sa.Integer(), nullable=True),
    sa.Column('shares', sa.Integer(), nullable=True),
    sa.Column('subscribersGained', sa.Integer(), nullable=True),
    sa.Column('subscribersLost', sa.Integer(), nullable=True),
    sa.Column('videosAddedToPlaylists', sa.Integer(), nullable=True),
    sa.Column('videosRemovedFromPlaylists', sa.Integer(), nullable=True),
    sa.Column('viewerPercentage', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('uploader_type',
    sa.Column('uploaderType', sa.String(length=50), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('views', sa.Integer(), nullable=True),
    sa.Column('adImpressions', sa.Integer(), nullable=True),
    sa.Column('annotationClickableImpressions', sa.Integer(), nullable=True),
    sa.Column('annotationClicks', sa.Integer(), nullable=True),
    sa.Column('annotationClickThroughRate', sa.Float(), nullable=True),
    sa.Column('annotationClosableImpressions', sa.Integer(), nullable=True),
    sa.Column('annotationCloses', sa.Integer(), nullable=True),
    sa.Column('annotationCloseRate', sa.Float(), nullable=True),
    sa.Column('annotationImpressions', sa.Integer(), nullable=True),
    sa.Column('audienceWatchRatio', sa.Float(), nullable=True),
    sa.Column('averageViewDuration', sa.Float(), nullable=True),
    sa.Column('averageViewPercentage', sa.Float(), nullable=True),
    sa.Column('cardClickRate', sa.Float(), nullable=True),
    sa.Column('cardClicks', sa.Integer(), nullable=True),
    sa.Column('cardImpressions', sa.Integer(), nullable=True),
    sa.Column('cardTeaserClickRate', sa.Float(), nullable=True),
    sa.Column('cardTeaserClicks', sa.Integer(), nullable=True),
    sa.Column('cardTeaserImpressions', sa.Integer(), nullable=True),
    sa.Column('comments', sa.Integer(), nullable=True),
    sa.Column('cpm', sa.Float(), nullable=True),
    sa.Column('dislikes', sa.Integer(), nullable=True),
    sa.Column('estimatedMinutesWatched', sa.Integer(), nullable=True),
    sa.Column('likes', sa.Integer(), nullable=True),
    sa.Column('playbackBasedCpm', sa.Float(), nullable=True),
    sa.Column('playlistStarts', sa.Integer(), nullable=True),
    sa.Column('savesAdded', sa.Integer(), nullable=True),
    sa.Column('savesRemoved', sa.Integer(), nullable=True),
    sa.Column('shares', sa.Integer(), nullable=True),
    sa.Column('subscribersGained', sa.Integer(), nullable=True),
    sa.Column('subscribersLost', sa.Integer(), nullable=True),
    sa.Column('videosAddedToPlaylists', sa.Integer(), nullable=True),
    sa.Column('videosRemovedFromPlaylists', sa.Integer(), nullable=True),
    sa.Column('viewerPercentage', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('video',
    sa.Column('video', sa.String(length=100), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('views', sa.Integer(), nullable=True),
    sa.Column('adImpressions', sa.Integer(), nullable=True),
    sa.Column('annotationClickableImpressions', sa.Integer(), nullable=True),
    sa.Column('annotationClicks', sa.Integer(), nullable=True),
    sa.Column('annotationClickThroughRate', sa.Float(), nullable=True),
    sa.Column('annotationClosableImpressions', sa.Integer(), nullable=True),
    sa.Column('annotationCloses', sa.Integer(), nullable=True),
    sa.Column('annotationCloseRate', sa.Float(), nullable=True),
    sa.Column('annotationImpressions', sa.Integer(), nullable=True),
    sa.Column('audienceWatchRatio', sa.Float(), nullable=True),
    sa.Column('averageViewDuration', sa.Float(), nullable=True),
    sa.Column('averageViewPercentage', sa.Float(), nullable=True),
    sa.Column('cardClickRate', sa.Float(), nullable=True),
    sa.Column('cardClicks', sa.Integer(), nullable=True),
    sa.Column('cardImpressions', sa.Integer(), nullable=True),
    sa.Column('cardTeaserClickRate', sa.Float(), nullable=True),
    sa.Column('cardTeaserClicks', sa.Integer(), nullable=True),
    sa.Column('cardTeaserImpressions', sa.Integer(), nullable=True),
    sa.Column('comments', sa.Integer(), nullable=True),
    sa.Column('cpm', sa.Float(), nullable=True),
    sa.Column('dislikes', sa.Integer(), nullable=True),
    sa.Column('estimatedMinutesWatched', sa.Integer(), nullable=True),
    sa.Column('likes', sa.Integer(), nullable=True),
    sa.Column('playbackBasedCpm', sa.Float(), nullable=True),
    sa.Column('playlistStarts', sa.Integer(), nullable=True),
    sa.Column('savesAdded', sa.Integer(), nullable=True),
    sa.Column('savesRemoved', sa.Integer(), nullable=True),
    sa.Column('shares', sa.Integer(), nullable=True),
    sa.Column('subscribersGained', sa.Integer(), nullable=True),
    sa.Column('subscribersLost', sa.Integer(), nullable=True),
    sa.Column('videosAddedToPlaylists', sa.Integer(), nullable=True),
    sa.Column('videosRemovedFromPlaylists', sa.Integer(), nullable=True),
    sa.Column('viewerPercentage', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('devicetype')
    with op.batch_alter_table('day', schema=None) as batch_op:
        batch_op.add_column(sa.Column('adImpressions', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('annotationClickableImpressions', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('annotationClicks', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('annotationClickThroughRate', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('annotationClosableImpressions', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('annotationCloses', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('annotationCloseRate', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('annotationImpressions', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('audienceWatchRatio', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('averageViewDuration', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('averageViewPercentage', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('cardClickRate', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('cardClicks', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('cardImpressions', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('cardTeaserClickRate', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('cardTeaserClicks', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('cardTeaserImpressions', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('estimatedMinutesWatched', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('playbackBasedCpm', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('playlistStarts', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('savesAdded', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('savesRemoved', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('subscribersGained', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('subscribersLost', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('videosAddedToPlaylists', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('videosRemovedFromPlaylists', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('viewerPercentage', sa.Float(), nullable=True))
        batch_op.drop_column('subscriberslost')
        batch_op.drop_column('annotationcloses')
        batch_op.drop_column('videosaddedtoplaylists')
        batch_op.drop_column('audiencewatchratio')
        batch_op.drop_column('annotationclicks')
        batch_op.drop_column('cardclickrate')
        batch_op.drop_column('cardclicks')
        batch_op.drop_column('adimpressions')
        batch_op.drop_column('savesremoved')
        batch_op.drop_column('videosremovedfromplaylists')
        batch_op.drop_column('averageviewpercentage')
        batch_op.drop_column('savesadded')
        batch_op.drop_column('cardimpressions')
        batch_op.drop_column('cardteaserclicks')
        batch_op.drop_column('playliststarts')
        batch_op.drop_column('averageviewduration')
        batch_op.drop_column('cardteaserimpressions')
        batch_op.drop_column('estimatedminuteswatched')
        batch_op.drop_column('annotationimpressions')
        batch_op.drop_column('playbackbasedcpm')
        batch_op.drop_column('annotationclosableimpressions')
        batch_op.drop_column('viewerpercentage')
        batch_op.drop_column('cardteaserclickrate')
        batch_op.drop_column('annotationclickthroughrate')
        batch_op.drop_column('annotationcloserate')
        batch_op.drop_column('annotationclickableimpressions')
        batch_op.drop_column('subscribersgained')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=sa.VARCHAR(length=60),
               type_=sa.String(length=255),
               existing_nullable=False)
        batch_op.alter_column('google_credentials',
               existing_type=postgresql.JSONB(astext_type=sa.Text()),
               type_=sa.JSON(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('google_credentials',
               existing_type=sa.JSON(),
               type_=postgresql.JSONB(astext_type=sa.Text()),
               existing_nullable=True)
        batch_op.alter_column('password_hash',
               existing_type=sa.String(length=255),
               type_=sa.VARCHAR(length=60),
               existing_nullable=False)

    with op.batch_alter_table('day', schema=None) as batch_op:
        batch_op.add_column(sa.Column('subscribersgained', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('annotationclickableimpressions', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('annotationcloserate', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('annotationclickthroughrate', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('cardteaserclickrate', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('viewerpercentage', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('annotationclosableimpressions', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('playbackbasedcpm', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('annotationimpressions', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('estimatedminuteswatched', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('cardteaserimpressions', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('averageviewduration', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('playliststarts', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('cardteaserclicks', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('cardimpressions', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('savesadded', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('averageviewpercentage', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('videosremovedfromplaylists', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('savesremoved', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('adimpressions', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('cardclicks', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('cardclickrate', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('annotationclicks', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('audiencewatchratio', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('videosaddedtoplaylists', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('annotationcloses', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('subscriberslost', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_column('viewerPercentage')
        batch_op.drop_column('videosRemovedFromPlaylists')
        batch_op.drop_column('videosAddedToPlaylists')
        batch_op.drop_column('subscribersLost')
        batch_op.drop_column('subscribersGained')
        batch_op.drop_column('savesRemoved')
        batch_op.drop_column('savesAdded')
        batch_op.drop_column('playlistStarts')
        batch_op.drop_column('playbackBasedCpm')
        batch_op.drop_column('estimatedMinutesWatched')
        batch_op.drop_column('cardTeaserImpressions')
        batch_op.drop_column('cardTeaserClicks')
        batch_op.drop_column('cardTeaserClickRate')
        batch_op.drop_column('cardImpressions')
        batch_op.drop_column('cardClicks')
        batch_op.drop_column('cardClickRate')
        batch_op.drop_column('averageViewPercentage')
        batch_op.drop_column('averageViewDuration')
        batch_op.drop_column('audienceWatchRatio')
        batch_op.drop_column('annotationImpressions')
        batch_op.drop_column('annotationCloseRate')
        batch_op.drop_column('annotationCloses')
        batch_op.drop_column('annotationClosableImpressions')
        batch_op.drop_column('annotationClickThroughRate')
        batch_op.drop_column('annotationClicks')
        batch_op.drop_column('annotationClickableImpressions')
        batch_op.drop_column('adImpressions')

    op.create_table('devicetype',
    sa.Column('devicetype', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('views', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('adimpressions', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('annotationclickableimpressions', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('annotationclicks', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('annotationclickthroughrate', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('annotationclosableimpressions', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('annotationcloses', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('annotationcloserate', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('annotationimpressions', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('audiencewatchratio', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('averageviewduration', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('averageviewpercentage', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('cardclickrate', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('cardclicks', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('cardimpressions', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('cardteaserclickrate', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('cardteaserclicks', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('cardteaserimpressions', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('comments', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('cpm', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('dislikes', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('estimatedminuteswatched', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('likes', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('playbackbasedcpm', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('playliststarts', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('savesadded', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('savesremoved', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('shares', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('subscribersgained', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('subscriberslost', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('videosaddedtoplaylists', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('videosremovedfromplaylists', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('viewerpercentage', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='devicetype_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='devicetype_pkey')
    )
    op.drop_table('video')
    op.drop_table('uploader_type')
    op.drop_table('sharing_service')
    op.drop_table('gender')
    op.drop_table('deviceType')
    # ### end Alembic commands ###