computer vision in IoT
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool TRUE
defaults write com.apple.desktopservices DSDontWriteUSBStores -bool TRUE
dot_clean -m /Volumes/4tb
sudo mdutil -i off /Volumes/4tb
touch /Volumes/4tb/.metadata_never_index
